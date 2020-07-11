import os
from dotenv import load_dotenv
from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware:
    """
    Checks each request for the Slack verification token. If absent, then the message did not come
    from Slack and is refused.
    """

    def __init__(self, app):
        load_dotenv()
        self.app = app
        self.token = os.environ['VERIFICATION_TOKEN']

    def __call__(self, environ, start_response):
        """
        Invokes the verification token middleware by checking in the header for the verification token sent
        by slack and returning a 403 message if the token is invalid.

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
