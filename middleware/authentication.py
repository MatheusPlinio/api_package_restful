from typing import Any
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class OAuth2AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        client_id = ''
        client_secret = ''

        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)

        token = oauth.fetch_token(token_url='https://example.com/token', client_id=client_id, client_secret=client_secret)

        request.headers['Authorization'] = 'Bearer' + token['access_token']

        response = self.get_response(request)

        return response