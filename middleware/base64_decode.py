from base64 import b64decode
from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware:
    """
    Checks each request for the Slack verification token. If absent, then the message did not come
    from Slack and is refused.
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        """
        Invokes the base64-decoding middleware to decode a request body if it's encoding using
        base64.

        :param environ: The request environment before beginning the middleware check.
        :param start_response: The initial response.
        :return: The resulting response after the middleware.
        """
        request = Request(environ)
        verification_token = request.headers.get('X-Slack-Signature', None)

        # if the token is missing or invalid, return a bad response
        if not verification_token or verification_token != self.token:
            res = Response(response={'message': 'invalid X-Slack-Signature header'},
                           mimetype='application/json',
                           status=401)
            return res(environ, start_response)

        return self.app(environ, start_response)
