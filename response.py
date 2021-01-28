import html
import json
from http import HTTPStatus
import magic

class Response():
    """
    Generic API Response
    """
    def success(self, content="OK", escape=False):
        """
        200
        """
        return self.response(status=HTTPStatus.OK, content=content, escape=escape)

    def bad_request(self, content={"message": "Bad request missing parameters"}, escape=False):
        """
        400
        """
        return self.response(status=HTTPStatus.BAD_REQUEST, content=content, escape=escape)

    def unauthorized(self, escape=False):
        """
        401
        """
        return self.response(status=HTTPStatus.UNAUTHORIZED, content={"message": "unauthorized"}, escape=escape)

    def not_found(self, escape=False):
        """
        404
        """
        return self.response(status=HTTPStatus.NOT_FOUND, content={"message" : "Not Found"}, escape=escape)

    def method_not_allowed(self, content="Method Not Allowed", escape=False):
        """
        405
        """
        return self.response(status=HTTPStatus.METHOD_NOT_ALLOWED, content=content, escape=escape)

    def error(self, escape=False):
        """
        500
        """
        return self.response(status=HTTPStatus.INTERNAL_SERVER_ERROR, content={"message" : "Internal Server Error"}, escape=escape)

    def no_content(self, escape=False):
        """
        204
        """
        return self.response(status=HTTPStatus.NO_CONTENT, content={"message" : "No Content"}, escape=escape)

    def conflict(self, escape=False):
        """
        409
        """
        return self.response(status=HTTPStatus.CONFLICT, content={"message": "Conflict"}, escape=escape)

    def response(self, status=HTTPStatus.OK, content=None, escape=False):
        """
        200
        """
        if isinstance(content, dict) or isinstance(content, list):
            content_type = "application/json"
            body = json.dumps(content)
        elif isinstance(content, str):
            content_type = "application/json"
            body = html.escape(content) if escape else content
        else:
            content_type = magic.from_buffer(content, mime=True)
            body = content
        return {
            "statusCode" : status.value,
            "statusDescription" : "HTTP " + status.phrase,
            "headers" : {
                "Content-Type" : content_type,
                "Access-Control-Allow-Origin" : "*"
            },
            "body" : body
        }