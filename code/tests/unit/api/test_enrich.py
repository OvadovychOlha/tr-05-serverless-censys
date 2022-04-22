from http import HTTPStatus
from unittest.mock import patch

from pytest import fixture
from requests.exceptions import SSLError
from censys.common.exceptions import CensysUnauthorizedException

from tests.unit.api.utils import get_headers
from tests.unit.conftest import mock_api_response
from tests.unit.payloads_for_tests import (
    EXPECTED_RESPONSE_OF_JWKS_ENDPOINT,
    EXPECTED_PAYLOAD_OF_CENSYS,
    base_payload,
    refer_payload,
)


def routes():
    yield '/observe/observables'
    yield '/refer/observables'


def ids():
    yield '73978e74-3497-4523-b6cf-45c778df6999'
    yield '61d25337-da63-47ca-97d5-b8e6e4630249'
    yield '792646ce-67c1-443c-b647-e148295aa5a3'
    yield 'd6b1e628-c24c-4302-8aec-1737ef6adba7'
    yield 'c1901f65-5f1f-477a-af30-ec6d9f5cfa4e'
    yield '7b7a9f34-2bf8-4339-8f54-cf972ae5ba3e'


@fixture(scope='module', params=routes(), ids=lambda route: f'POST {route}')
def route(request):
    return request.param


@fixture(scope='module')
def invalid_json_value():
    return [{'type': 'ip', 'value': ''}]


@patch('requests.get')
def test_enrich_call_with_valid_jwt_but_invalid_json_value(
        mock_request,
        route, client, valid_jwt, invalid_json_value,
        invalid_json_expected_payload
):
    mock_request.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    response = client.post(route,
                           headers=get_headers(valid_jwt()),
                           json=invalid_json_value)
    assert response.status_code == HTTPStatus.OK
    assert response.json == invalid_json_expected_payload(
        "{0: {'value': ['Field may not be blank.']}}"
    )


@fixture(scope='module')
def valid_json():
    return [{'type': 'ip', 'value': '1.1.1.1'}]


@patch('api.mapping.uuid4')
@patch('requests.get')
@patch('api.client.CensysHosts.view_host_events')
def test_enrich_call_success(mock_events, mock_request, mock_ids,
                             route, client, valid_jwt, valid_json):
    mock_request.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    mock_events.side_effect = [EXPECTED_PAYLOAD_OF_CENSYS]
    mock_ids.side_effect = ids()
    response = client.post(route, headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    if route == '/observe/observables':
        assert response.json == base_payload()
    elif route == '/refer/observables':
        assert response.json == refer_payload()


@patch('api.client.CensysHosts.view_host_events')
@patch('requests.get')
def test_enrich_call_with_ssl_error(mock_get, mock_request,
                                    mock_exception_for_ssl_error,
                                    client, valid_jwt, valid_json,
                                    ssl_error_expected_relay_response):

    mock_get.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    mock_request.side_effect = [SSLError(mock_exception_for_ssl_error)]

    response = client.post('/observe/observables',
                           headers=get_headers(valid_jwt()), json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == ssl_error_expected_relay_response


@patch('api.client.CensysHosts.view_host_events')
@patch('requests.get')
def test_enrich_call_with_unauthorized_error(
        mock_get, mock_request,
        client, valid_jwt, valid_json,
        authorization_error_expected_relay_response):

    mock_get.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    mock_request.side_effect = [CensysUnauthorizedException(
        403,
        'Unauthorized. You must authenticate with a valid API ID and secret.',
        const='unauthorized')]

    response = client.post('/observe/observables',
                           headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_error_expected_relay_response
