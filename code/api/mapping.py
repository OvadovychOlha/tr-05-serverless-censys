from uuid import uuid4

SIGHTING = 'sighting'

SIGHTING_DEFAULTS = {
    'count': 1,
    'schema_version': '1.1.11',
    'internal': True,
    'confidence': 'High',
    'type': SIGHTING,
    'source': 'Censys',
}


class Sighting:
    def __init__(self, observable):
        self.observable = observable

    def _title(self):
        return f'Event for {self.observable["value"]} observed by Censys'

    @staticmethod
    def _transient_id(entity, uuid=None):
        if uuid is None:
            uuid = uuid4()
        return f"transient:{entity}-{uuid}"

    @staticmethod
    def _observed_time(event_details, event):
        try:
            observed_time = event_details['observed_at']
        except KeyError:
            observed_time = event['timestamp']
        return {
            'start_time': observed_time
        }

    @staticmethod
    def _make_data_table(message):
        data = {
            'columns': [],
            'rows': [[]]
        }

        for key, value in message.items():
            data['columns'].append({'name': key, 'type': 'string'})
            data['rows'][0].append(str(value))

        return data

    @staticmethod
    def _short_description(event):
        return f'Event {event["_event"]} observed at Censys'

    def _description(self, event):
        return f'Event {event["_event"]} for ' \
               f'{self.observable["value"]} observed at Censys'

    @staticmethod
    def _get_event_details(event):
        if 'service_observed' in event:
            return event['service_observed']
        elif 'location_updated' in event:
            return event['location_updated']
        elif 'routing_updated' in event:
            return event['routing_updated']
        elif 'service_removed_from_host' in event:
            return event['service_removed_from_host']
        elif 'service_added_to_host' in event:
            return event['service_added_to_host']

    def extract(self, event):
        event_details = self._get_event_details(event)
        sighting = {
            'id': self._transient_id(SIGHTING),
            'observed_time': self._observed_time(event_details, event),
            'observables': [self.observable],
            'short_description': self._short_description(event),
            'description': self._description(event),
            'data': self._make_data_table(event),
            'title': self._title(),
            **SIGHTING_DEFAULTS,
        }

        return sighting
