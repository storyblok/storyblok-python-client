from .http_client import HttpClient

# Assign all the api classes
from .api.spaces import Spaces
from .api.stories import Stories
from .api.tags import Tags
from .api.links import Links
from .api.datasource_entries import DatasourceEntries
from .api.datasources import Datasources

class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def spaces(self):
        """Returns your current space name, published version and domain
        """
        return Spaces(self.http_client)

    def stories(self):
        """Returns stories api instance
        """
        return Stories(self.http_client)

    def tags(self):
        """Returns tags api instance
        """
        return Tags(self.http_client)

    def links(self):
        """Returns links api instance
        """
        return Links(self.http_client)

    def datasources(self):
        """Returns Datasources api instance
        """
        return Datasources(self.http_client)

    def datasource_entries(self):
        """Returns DatasourceEntries api instance
        """
        return DatasourceEntries(self.http_client)

    def get(self, path, token='', auth_token='', params={}, options={}):
      """ Makes a custom get request
      """

      if(token):
        params['token'] = token
      else:
        options['headers'] = {'Authorization': auth_token }

      res = self.http_client.get(path, params, options)
      return res
