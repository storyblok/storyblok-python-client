class AuthHandler(object):

    """AuthHandler takes care of devising the auth type and using it"""

    def __init__(self, auth):
        self.auth = auth

    def get_auth_type(self):
        """Calculating the Authentication Type"""

        return -1

    def set(self, request):
        if len(self.auth.keys()) == 0:
            return request

        auth = self.get_auth_type()
        flag = False

        if not flag:
            raise StandardError("Unable to calculate authorization method. Please check")

        return request

