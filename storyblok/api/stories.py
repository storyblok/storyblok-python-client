from .param_adapter import body

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
        response = self.client.get('/cdn/stories/', body(token, options), options)

        return response

    def single(self, token, story_id, options={}):
        """Returns a single story by id (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-story-by-id)

        '/cdn/stories/:story_id' GET

        Args:
            token: Public token for published or private token for draft version
            story_id: The Id of the story that you want to get
        """

        response = self.client.get('/cdn/stories/' + story_id, body(token, options), options)

        return response

