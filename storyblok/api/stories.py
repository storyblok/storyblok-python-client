class Stories(object):

    """Returns stories api instance
    """

    def __init__(self, client):
        self.client = client

    def list(self, token, options={}):
        """Returns a list of Stories (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-list-of-stories)

        '/cdn/stories/' GET

        Args:
            token: Public token for published or private token for draft version
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/cdn/stories/', body, options)

        return response

    def single(self, token, options={}):
        """Returns a single story by id (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-story-by-id)

        '/cdn/stories/:story_id' GET

        Args:
            token: Public token for published or private token for draft version
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('/cdn/stories/' + story_id + '', body, options)

        return response

