from functools import partial

from flask import g, Blueprint

from api.client import CensysClient
from api.mapping import Sighting
from api.schemas import ObservableSchema
from api.utils import get_json, get_credentials, jsonify_data, jsonify_result

enrich_api = Blueprint('enrich', __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route('/observe/observables', methods=['POST'])
def observe_observables():
    credentials = get_credentials()
    observables = get_observables()

    g.sightings = []
    client = CensysClient(credentials)

    for observable in observables:
        events = client.get_events(observable)
        mapping = Sighting(observable)

        for event in events:
            sighting = mapping.extract(event)
            g.sightings.append(sighting)

    return jsonify_result()


@enrich_api.route('/refer/observables', methods=['POST'])
def refer_observables():
    _ = get_credentials()
    observables = get_observables()

    relay_output = [
        {
            'id': (f'ref-censys-search-{observable["type"].replace("_", "-")}'
                   f'-{observable["value"]}'),
            'title': 'Events for this IP',
            'description':
                f'Events for this {observable["type"]} in the Censys',
            'url': f'https://search.censys.io/hosts/{observable["value"]}'
                   '/events',
            'categories': ['Censys', 'Search', 'Events'],
        }
        for observable in observables
    ]

    return jsonify_data(relay_output)
