class Event():
    """
    Generic event class
    """
    def __init__(self, event):
        self._payload = event["body"]
        self._query_strings = event["queryStringParameters"]
        self._path = event["path"].strip("\\/").split("")
        self._type = event["httpMethod"]
        self._headers = event["headers"]

        def get_request_method(self):
            """
            Get the request type
            """
            return self._type

        def get_headers(self):
            """
            Get the headers
            """
            return self._headers

        def get_path(self):
            """
            Get the path
            """
            return self._path
        
        def get_payload(self):
            """
            Get the path
            """
            return self._payload
        
        def get_query_strings(self):
            """
            Get the path
            """
            return self._query_strings