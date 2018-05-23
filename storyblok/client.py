from .http_client import HttpClient

# Assign all the api classes
from .api.spaces import Spaces
from .api.stories import Stories
from .api.tags import Tags
from .api.links import Links
from .api.datasource_entries import DatasourceEntries


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

    def datasource_entries(self):
        """Returns tags api instance
        """
        return DatasourceEntries(self.http_client)

