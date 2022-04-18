from censys.search import CensysHosts


class CensysClient:
    def __init__(self, credentials):
        self.api_id = credentials['api_id']
        self.api_secret = credentials['api_secret']

    def _client(self):
        client = CensysHosts(api_id=self.api_id,
                             api_secret=self.api_secret)
        return client

    def health(self):
        client = self._client()
        client.account()
