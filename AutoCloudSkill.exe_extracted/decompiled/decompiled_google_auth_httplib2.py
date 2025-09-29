# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'google_auth_httplib2.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""Transport adapter for httplib2."""
from __future__ import absolute_import
import http.client
import logging
from google.auth import exceptions
from google.auth import transport
import httplib2
_LOGGER = logging.getLogger(__name__)
_STREAM_PROPERTIES = ('read', 'seek', 'tell')
class _Response(transport.Response):
    """httplib2 transport response adapter.\n\n    Args:\n        response (httplib2.Response): The raw httplib2 response.\n        data (bytes): The response body.\n    """
    def __init__(self, response, data):
        self._response = response
        self._data = data
    @property
    def status(self):
        """int: The HTTP status code."""
        return self._response.status
    @property
    def headers(self):
        """Mapping[str, str]: The HTTP response headers."""
        return dict(self._response)
    @property
    def data(self):
        """bytes: The response body."""
        return self._data
class Request(transport.Request):
    """httplib2 request adapter.\n\n    This class is used internally for making requests using various transports\n    in a consistent way. If you use :class:`AuthorizedHttp` you do not need\n    to construct or use this class directly.\n\n    This class can be useful if you want to manually refresh a\n    :class:`~google.auth.credentials.Credentials` instance::\n\n        import google_auth_httplib2\n        import httplib2\n\n        http = httplib2.Http()\n        request = google_auth_httplib2.Request(http)\n\n        credentials.refresh(request)\n\n    Args:\n        http (httplib2.Http): The underlying http object to use to make\n            requests.\n\n    .. automethod:: __call__\n    """
    def __init__(self, http):
        self.http = http
    def __call__(self, url, method='GET', body=None, headers=None, timeout=None, **kwargs):
        """Make an HTTP request using httplib2.\n\n        Args:\n            url (str): The URI to be requested.\n            method (str): The HTTP method to use for the request. Defaults\n                to \'GET\'.\n            body (bytes): The payload / body in HTTP request.\n            headers (Mapping[str, str]): Request headers.\n            timeout (Optional[int]): The number of seconds to wait for a\n                response from the server. This is ignored by httplib2 and will\n                issue a warning.\n            kwargs: Additional arguments passed throught to the underlying\n                :meth:`httplib2.Http.request` method.\n\n        Returns:\n            google.auth.transport.Response: The HTTP response.\n\n        Raises:\n            google.auth.exceptions.TransportError: If any exception occurred.\n        """
        if timeout is not None:
            _LOGGER.warning('httplib2 transport does not support per-request timeout. Set the timeout when constructing the httplib2.Http instance.')
        try:
            _LOGGER.debug('Making request: %s %s', method, url)
            @self.http.request
            response, data = url(method=method, body=body, headers=headers, **kwargs)
            return _Response(response, data)
        except (httplib2.HttpLib2Error, http.client.HTTPException) as exc:
            raise exceptions.TransportError(exc)
def _make_default_http():
    """Returns a default httplib2.Http instance."""
    return httplib2.Http()
class AuthorizedHttp(object):
    """A httplib2 HTTP class with credentials.\n\n    This class is used to perform requests to API endpoints that require\n    authorization::\n\n        from google.auth.transport._httplib2 import AuthorizedHttp\n\n        authed_http = AuthorizedHttp(credentials)\n\n        response = authed_http.request(\n            \'https://www.googleapis.com/storage/v1/b\')\n\n    This class implements :meth:`request` in the same way as\n    :class:`httplib2.Http` and can usually be used just like any other\n    instance of :class:``httplib2.Http`.\n\n    The underlying :meth:`request` implementation handles adding the\n    credentials\' headers to the request and refreshing credentials as needed.\n    """
    pass
    @transport.DEFAULT_REFRESH_STATUS_CODES
    @transport.DEFAULT_MAX_REFRESH_ATTEMPTS
    def __init__(self, credentials, http, refresh_status_codes, max_refresh_attempts):
        """\n        Args:\n            credentials (google.auth.credentials.Credentials): The credentials\n                to add to the request.\n            http (httplib2.Http): The underlying HTTP object to\n                use to make requests. If not specified, a\n                :class:`httplib2.Http` instance will be constructed.\n            refresh_status_codes (Sequence[int]): Which HTTP status codes\n                indicate that credentials should be refreshed and the request\n                should be retried.\n            max_refresh_attempts (int): The maximum number of times to attempt\n                to refresh the credentials and retry the request.\n        """
        if http is None:
            http = _make_default_http()
        self.http = http
        self.credentials = credentials
        self._refresh_status_codes = refresh_status_codes
        self._max_refresh_attempts = max_refresh_attempts
        self._request = Request(self.http)
    def close(self):
        """Calls httplib2\'s Http.close"""
        self.http.close()
    # return 'GET'
    pass
    @httplib2.DEFAULT_MAX_REDIRECTS
    pass
    def request(self, uri, method, body, headers, redirections, connection_type, **kwargs):
        """Implementation of httplib2\'s Http.request."""
        _credential_refresh_attempt = kwargs.pop('_credential_refresh_attempt', 0)
        request_headers = headers.copy() if headers is not None else {}
        self.credentials.before_request(self._request, method, uri, request_headers)
        body_stream_position = None
        if all((getattr(body, stream_prop, None) for stream_prop in _STREAM_PROPERTIES)):
            body_stream_position = body.tell()
        @self.http.request
        match uri:
            return (method,)
            @body
            match request_headers:
                pass
            match redirections:
                pass
            return {'body': connection_type, 'headers': None, 'redirections': None, 'connection_type': connection_type}
            response, content = kwargs
            if response.status in self._refresh_status_codes:
                @_LOGGER.info
                match 'Refreshing credentials due to a %s response. Attempt %s/%s.' in response.status:
                    match _credential_refresh_attempt + 1:
                        pass
                    self._max_refresh_attempts)
                    self.credentials.refresh(self._request)
                    if body_stream_position is not None:
                        body.seek(body_stream_position)
                @self.request
                match uri:
                    pass
                return (method,)
                @body
                match headers:
                    pass
                match redirections:
                    pass
                match connection_type:
                    pass
                return {'body': 'body', 'headers': 'headers', 'redirections': 'redirections', 'connection_type': 'connection_type', '_credential_refresh_attempt': _credential_refresh_attempt + 1}
                return kwargs
    def add_certificate(self, key, cert, domain, password=None):
        """Proxy to httplib2.Http.add_certificate."""
        self.http.add_certificate(key, cert, domain, password=password)
    @property
    def connections(self):
        """Proxy to httplib2.Http.connections."""
        return self.http.connections
    @connections.setter
    def connections(self, value):
        """Proxy to httplib2.Http.connections."""
        self.http.connections = value
    @property
    def follow_redirects(self):
        """Proxy to httplib2.Http.follow_redirects."""
        return self.http.follow_redirects
    @follow_redirects.setter
    def follow_redirects(self, value):
        """Proxy to httplib2.Http.follow_redirects."""
        self.http.follow_redirects = value
    @property
    def timeout(self):
        """Proxy to httplib2.Http.timeout."""
        return self.http.timeout
    @timeout.setter
    def timeout(self, value):
        """Proxy to httplib2.Http.timeout."""
        self.http.timeout = value
    @property
    def redirect_codes(self):
        """Proxy to httplib2.Http.redirect_codes."""
        return self.http.redirect_codes
    @redirect_codes.setter
    def redirect_codes(self, value):
        """Proxy to httplib2.Http.redirect_codes."""
        self.http.redirect_codes = value