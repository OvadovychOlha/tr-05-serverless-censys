EXPECTED_RESPONSE_OF_JWKS_ENDPOINT = {
  'keys': [
    {
      'kty': 'RSA',
      'n': 'tSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V'
           'mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H'
           'vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17'
           '_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB'
           'Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7'
           '33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke'
           'Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2'
           'Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8'
           'uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M'
           'loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU'
           'jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM'
           '-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35'
           'YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR'
           'k3jNdVM',
      'e': 'AQAB',
      'alg': 'RS256',
      'kid': '02B1174234C29F8EFB69911438F597FF3FFEE6B7',
      'use': 'sig'
    }
  ]
}

RESPONSE_OF_JWKS_ENDPOINT_WITH_WRONG_KEY = {
    'keys': [
        {
            'kty': 'RSA',
            'n': 'pSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V'
                 'mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H'
                 'vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17'
                 '_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB'
                 'Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7'
                 '33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke'
                 'Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2'
                 'Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8'
                 'uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M'
                 'loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU'
                 'jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM'
                 '-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35'
                 'YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR'
                 'k3jNdVM',
            'e': 'AQAB',
            'alg': 'RS256',
            'kid': '02B1174234C29F8EFB69911438F597FF3FFEE6B7',
            'use': 'sig'
        }
    ]
}

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

EXPECTED_PAYLOAD_OF_CENSYS = [
    {
        "timestamp": "2022-04-14T07:32:19.409Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:32:19.382893452Z",
            "perspective_id": "PERSPECTIVE_NTT",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:32:30.369Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:32:29.719301999Z",
            "perspective_id": "PERSPECTIVE_TATA",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:33:20.100Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:33:20.042583206Z",
            "perspective_id": "PERSPECTIVE_HE",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:34:18.017Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:34:17.958692540Z",
            "perspective_id": "PERSPECTIVE_NTT",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:34:26.128Z",
        "service_observed": {
            "id": {
                "port": 80,
                "service_name": "HTTP",
                "transport_protocol": "TCP"
            },
            "observed_at": "2022-04-14T07:34:26.070569439Z",
            "perspective_id": "PERSPECTIVE_HE",
            "changed_fields": [
                {
                    "field_name": "http.response.headers.Cf-Ray.headers"
                },
                {
                    "field_name": "banner"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:34:26.183Z",
        "service_observed": {
            "id": {
                "port": 443,
                "service_name": "HTTP",
                "transport_protocol": "TCP"
            },
            "observed_at": "2022-04-14T07:34:26.075740583Z",
            "perspective_id": "PERSPECTIVE_HE",
            "changed_fields": [
                {
                    "field_name":
                        "http.response.headers.X-Amz-Request-Id.headers"
                },
                {
                    "field_name": "http.response.status_reason"
                },
                {
                    "field_name": "http.response.headers.Location.headers"
                },
                {
                    "field_name": "http.response.body_size"
                },
                {
                    "field_name":
                        "http.response.headers.X-Rgw-Object-Type.headers"
                },
                {
                    "field_name":
                        "http.response.headers.Served-In-Seconds.headers"
                },
                {
                    "field_name": "http.response.html_tags"
                },
                {
                    "field_name": "http.request.uri"
                },
                {
                    "field_name": "banner"
                },
                {
                    "field_name": "http.response.headers.Expires.headers"
                },
                {
                    "field_name": "http.response.headers.Cf-Ray.headers"
                },
                {
                    "field_name": "http.response.headers.Report-To.headers"
                },
                {
                    "field_name": "http.response.headers.Age.headers"
                },
                {
                    "field_name": "http.response.status_code"
                },
                {
                    "field_name": "http.response.headers.Set-Cookie.headers"
                },
                {
                    "field_name": "http.response.headers.Last-Modified.headers"
                },
                {
                    "field_name": "http.body_hash"
                },
                {
                    "field_name": "http.response.body"
                }
            ]
        },
        "_event": "service_observed"
    }
]


def base_payload():
    return {
        'data':
            {
                'sightings': {
                    'count': 6,
                    'docs': [
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}],
                                'rows': [['2022-04-14T07:32:19.409Z',
                                          "{'id': {'port': 53, 'transport_pro"
                                          "tocol': 'UDP', 'service_name': 'DN"
                                          "S'}, 'observed_at': '2022-04-14T07"
                                          ":32:19.382893452Z', 'perspective_i"
                                          "d': 'PERSPECTIVE_NTT', 'changed_fi"
                                          "elds': [{'field_name': 'dns.answer"
                                          "s'}]}",
                                          'service_observed']
                                         ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-73978e74-3497-4523-b6cf'
                                  '-45c778df6999',
                            'internal': True,
                            'observables': [{'type': 'ip',
                                             'value': '1.1.1.1'}],
                            'observed_time': {
                                'start_time':
                                    '2022-04-14T07:32:19.382893452Z'},
                            'schema_version': '1.1.11',
                            'short_description': 'Event service_observed obse'
                                                 'rved at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'},
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [{'name': 'timestamp',
                                             'type': 'string'},
                                            {'name': 'service_observed',
                                             'type': 'string'},
                                            {'name': '_event',
                                             'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:32:30.369Z',
                                     "{'id': {'port': 53, 'transport_protocol"
                                     "': 'UDP', 'service_name': 'DNS'}, 'obse"
                                     "rved_at': '2022-04-14T07:32:29.71930199"
                                     "9Z', 'perspective_id': 'PERSPECTIVE_TAT"
                                     "A', 'changed_fields': [{'field_name': '"
                                     "dns.answers'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-61d25337-da63-47ca-97d5'
                                  '-b8e6e4630249',
                            'internal': True,
                            'observables': [{'type': 'ip',
                                             'value': '1.1.1.1'}],
                            'observed_time': {
                                'start_time':
                                    '2022-04-14T07:32:29.719301999Z'},
                            'schema_version': '1.1.11',
                            'short_description': 'Event service_observed obse'
                                                 'rved at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'},
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [{'name': 'timestamp',
                                             'type': 'string'},
                                            {'name': 'service_observed',
                                             'type': 'string'},
                                            {'name': '_event',
                                             'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:33:20.100Z',
                                     "{'id': {'port': 53, 'transport_protocol"
                                     "': 'UDP', 'service_name': 'DNS'}, 'obse"
                                     "rved_at': '2022-04-14T07:33:20.04258320"
                                     "6Z', 'perspective_id': 'PERSPECTIVE_HE'"
                                     ", 'changed_fields': [{'field_name': 'dn"
                                     "s.answers'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-792646ce-67c1-443c-b647'
                                  '-e148295aa5a3',
                            'internal': True,
                            'observables': [{'type': 'ip',
                                             'value': '1.1.1.1'}],
                            'observed_time': {
                                'start_time': '2022-04-14T07:33:20.042583206Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description':
                                'Event service_observed observed at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'
                        },
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:34:18.017Z',
                                     "{'id': {'port': 53, 'transport_protocol"
                                     "': 'UDP', 'service_name': 'DNS'}, 'obse"
                                     "rved_at': '2022-04-14T07:34:17.95869254"
                                     "0Z', 'perspective_id': 'PERSPECTIVE_NTT"
                                     "', 'changed_fields': [{'field_name': 'd"
                                     "ns.answers'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-d6b1e628-c24c-4302-8aec'
                                  '-1737ef6adba7',
                            'internal': True,
                            'observables': [
                                {'type': 'ip', 'value': '1.1.1.1'}
                            ],
                            'observed_time': {
                                'start_time': '2022-04-14T07:34:17.958692540Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description':
                                'Event service_observed observed at Censys',
                            'source': 'Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'type': 'sighting'
                        },
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:34:26.128Z',
                                     "{'id': {'port': 80, 'service_name': 'HT"
                                     "TP', 'transport_protocol': 'TCP'}, 'obs"
                                     "erved_at': '2022-04-14T07:34:26.0705694"
                                     "39Z', 'perspective_id': 'PERSPECTIVE_HE"
                                     "', 'changed_fields': [{'field_name': 'h"
                                     "ttp.response.headers.Cf-Ray.headers'}, "
                                     "{'field_name': 'banner'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-c1901f65-5f1f-477a-af30'
                                  '-ec6d9f5cfa4e',
                            'internal': True,
                            'observables': [
                                {'type': 'ip', 'value': '1.1.1.1'}
                            ],
                            'observed_time': {
                                'start_time':
                                    '2022-04-14T07:34:26.070569439Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description':
                                'Event service_observed observed at Censys',
                            'source': 'Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'type': 'sighting'
                        },
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}
                                ],
                                'rows': [
                                    ['2022-04-14T07:34:26.183Z',
                                     "{'id': {'port': 443, 'service_name': 'H"
                                     "TTP', 'transport_protocol': 'TCP'}, 'ob"
                                     "served_at': '2022-04-14T07:34:26.075740"
                                     "583Z', 'perspective_id': 'PERSPECTIVE_H"
                                     "E', 'changed_fields': [{'field_name': '"
                                     "http.response.headers.X-Amz-Request-Id."
                                     "headers'}, {'field_name': 'http.respons"
                                     "e.status_reason'}, {'field_name': 'http"
                                     ".response.headers.Location.headers'}, {"
                                     "'field_name': 'http.response.body_size'"
                                     "}, {'field_name': 'http.response.header"
                                     "s.X-Rgw-Object-Type.headers'}, {'field_"
                                     "name': 'http.response.headers.Served-In"
                                     "-Seconds.headers'}, {'field_name': 'htt"
                                     "p.response.html_tags'}, {'field_name': "
                                     "'http.request.uri'}, {'field_name': 'ba"
                                     "nner'}, {'field_name': 'http.response.h"
                                     "eaders.Expires.headers'}, {'field_name'"
                                     ": 'http.response.headers.Cf-Ray.headers"
                                     "'}, {'field_name': 'http.response.heade"
                                     "rs.Report-To.headers'}, {'field_name': "
                                     "'http.response.headers.Age.headers'}, {"
                                     "'field_name': 'http.response.status_cod"
                                     "e'}, {'field_name': 'http.response.head"
                                     "ers.Set-Cookie.headers'}, {'field_name'"
                                     ": 'http.response.headers.Last-Modified."
                                     "headers'}, {'field_name': 'http.body_ha"
                                     "sh'}, {'field_name': 'http.response.bod"
                                     "y'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-7b7a9f34-2bf8-4339-8f54'
                                  '-cf972ae5ba3e',
                            'internal': True,
                            'observables': [
                                {'type': 'ip', 'value': '1.1.1.1'}
                            ],
                            'observed_time': {
                                'start_time': '2022-04-14T07:34:26.075740583Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description': 'Event service_observed obse'
                                                 'rved at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'}
                    ]
                }
            }
    }
