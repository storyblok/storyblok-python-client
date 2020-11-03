class DatasourceEntries(object):

    """Returns DatasourceEntries api instance
    """

    def __init__(self, client):
        self.client = client

    def list(self, token, options={}):
        """Returns a list of DatasourceEntries (https://www.storyblok.com/docs/api/content-delivery#core-resources/datasource-entries/datasource-entries)

        '/cdn/datasource_entries/' GET

        Args:
            token: Public token for published or private token for draft version
        """
        body = options['query'] if 'query' in options else {}
        body['token'] = token

        response = self.client.get('/cdn/datasource_entries/', body, options)

        return response

