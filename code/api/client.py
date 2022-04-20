from censys.search import CensysHosts

from api.utils import catch_errors


class CensysClient:
    def __init__(self, credentials):
        self.api_id = credentials['api_id']
        self.api_secret = credentials['api_secret']

    def _client(self):
        client = CensysHosts(api_id=self.api_id,
                             api_secret=self.api_secret)
        return client

    @catch_errors
    def health(self):
        client = self._client()
        response = client.account()
        return response

    @catch_errors
    def get_events(self, observable):
        client = self._client()
        events = client.view_host_events(observable['value'])

        return events
