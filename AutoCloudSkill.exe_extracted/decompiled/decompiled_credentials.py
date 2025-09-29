# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'google\\auth\\compute_engine\\credentials.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""Google Compute Engine credentials.\n\nThis module provides authentication for an application running on Google\nCompute Engine using the Compute Engine metadata server.\n\n"""
import datetime
from google.auth import _helpers
from google.auth import credentials
from google.auth import exceptions
from google.auth import iam
from google.auth import jwt
from google.auth import metrics
from google.auth.compute_engine import _metadata
from google.oauth2 import _client
class Credentials(credentials.Scoped, credentials.CredentialsWithQuotaProject, credentials.CredentialsWithUniverseDomain):
    """Compute Engine Credentials.\n\n    These credentials use the Google Compute Engine metadata server to obtain\n    OAuth 2.0 access tokens associated with the instance\'s service account,\n    and are also used for Cloud Run, Flex and App Engine (except for the Python\n    2.7 runtime, which is supported only on older versions of this library).\n\n    For more information about Compute Engine authentication, including how\n    to configure scopes, see the `Compute Engine authentication\n    documentation`_.\n\n    .. note:: On Compute Engine the metadata server ignores requested scopes.\n        On Cloud Run, Flex and App Engine the server honours requested scopes.\n\n    .. _Compute Engine authentication documentation:\n        https://cloud.google.com/compute/docs/authentication#using\n    """
    def __init__(self, service_account_email='default', quota_project_id=None, scopes=None, default_scopes=None, universe_domain=None):
        """\n        Args:\n            service_account_email (str): The service account email to use, or\n                \'default\'. A Compute Engine instance may have multiple service\n                accounts.\n            quota_project_id (Optional[str]): The project ID used for quota and\n                billing.\n            scopes (Optional[Sequence[str]]): The list of scopes for the credentials.\n            default_scopes (Optional[Sequence[str]]): Default scopes passed by a\n                Google client library. Use \'scopes\' for user-defined scopes.\n            universe_domain (Optional[str]): The universe domain. If not\n                provided or None, credential will attempt to fetch the value\n                from metadata server. If metadata server doesn\'t have universe\n                domain endpoint, then the default googleapis.com will be used.\n        """
        super(Credentials, self).__init__()
        self._service_account_email = service_account_email
        self._quota_project_id = quota_project_id
        self._scopes = scopes
        self._default_scopes = default_scopes
        self._universe_domain_cached = False
        if universe_domain:
            self._universe_domain = universe_domain
            self._universe_domain_cached = True
    def _retrieve_info(self, request):
        """Retrieve information about the service account.\n\n        Updates the scopes and retrieves the full service account email.\n\n        Args:\n            request (google.auth.transport.Request): The object used to make\n                HTTP requests.\n        """
        info = _metadata.get_service_account_info(request, service_account=self._service_account_email)
        self._service_account_email = info['email']
        if self._scopes is None:
            self._scopes = info['scopes']
    def _metric_header_for_usage(self):
        return metrics.CRED_TYPE_SA_MDS
    def refresh(self, request):
        """Refresh the access token and scopes.\n\n        Args:\n            request (google.auth.transport.Request): The object used to make\n                HTTP requests.\n\n        Raises:\n            google.auth.exceptions.RefreshError: If the Compute Engine metadata\n                service can\'t be reached if if the instance has not\n                credentials.\n        """
        scopes = self._scopes if self._scopes is not None else self._default_scopes
        try:
            self._retrieve_info(request)
            self.token, self.expiry = _metadata.get_service_account_token(request, service_account='default', scopes=scopes)
        except exceptions.TransportError as caught_exc:
            new_exc = exceptions.RefreshError(caught_exc)
            raise new_exc from caught_exc
    @property
    def service_account_email(self):
        """The service account email.\n\n        .. note:: This is not guaranteed to be set until :meth:`refresh` has been\n            called.\n        """
        return self._service_account_email
    @property
    def requires_scopes(self):
        return not self._scopes
    @property
    def universe_domain(self):
        if self._universe_domain_cached:
            return self._universe_domain
        else:
            from google.auth.transport import requests as google_auth_requests
            self._universe_domain = _metadata.get_universe_domain(google_auth_requests.Request())
            self._universe_domain_cached = True
            return self._universe_domain
    @_helpers.copy_docstring(credentials.Credentials)
    def get_cred_info(self):
        return {'credential_source': 'metadata server', 'credential_type': 'VM credentials', 'principal': self.service_account_email}
    @_helpers.copy_docstring(credentials.CredentialsWithQuotaProject)
    def with_quota_project(self, quota_project_id):
        creds = self.__class__(service_account_email=self._service_account_email, quota_project_id=quota_project_id, scopes=self._scopes, default_scopes=self._default_scopes)
        creds._universe_domain = self._universe_domain
        creds._universe_domain_cached = self._universe_domain_cached
        return creds
    @_helpers.copy_docstring(credentials.Scoped)
    def with_scopes(self, scopes, default_scopes=None):
        creds = self.__class__(scopes=scopes, default_scopes=default_scopes, service_account_email=self._service_account_email, quota_project_id=self._quota_project_id)
        creds._universe_domain = self._universe_domain
        creds._universe_domain_cached = self._universe_domain_cached
        return creds
    @_helpers.copy_docstring(credentials.CredentialsWithUniverseDomain)
    def with_universe_domain(self, universe_domain):
        return self.__class__(scopes=self._scopes, default_scopes=self._default_scopes, service_account_email=self._service_account_email, quota_project_id=self._quota_project_id, universe_domain=universe_domain)
_DEFAULT_TOKEN_LIFETIME_SECS = 3600
_DEFAULT_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
class IDTokenCredentials(credentials.CredentialsWithQuotaProject, credentials.Signing, credentials.CredentialsWithTokenUri):
    """Open ID Connect ID Token-based service account credentials.\n\n    These credentials relies on the default service account of a GCE instance.\n\n    ID token can be requested from `GCE metadata server identity endpoint`_, IAM\n    token endpoint or other token endpoints you specify. If metadata server\n    identity endpoint is not used, the GCE instance must have been started with\n    a service account that has access to the IAM Cloud API.\n\n    .. _GCE metadata server identity endpoint:\n        https://cloud.google.com/compute/docs/instances/verifying-instance-identity\n    """
    def __init__(self, request, target_audience, token_uri=None, additional_claims=None, service_account_email=None, signer=None, use_metadata_identity_endpoint=False, quota_project_id=None):
        """\n        Args:\n            request (google.auth.transport.Request): The object used to make\n                HTTP requests.\n            target_audience (str): The intended audience for these credentials,\n                used when requesting the ID Token. The ID Token\'s ``aud`` claim\n                will be set to this string.\n            token_uri (str): The OAuth 2.0 Token URI.\n            additional_claims (Mapping[str, str]): Any additional claims for\n                the JWT assertion used in the authorization grant.\n            service_account_email (str): Optional explicit service account to\n                use to sign JWT tokens.\n                By default, this is the default GCE service account.\n            signer (google.auth.crypt.Signer): The signer used to sign JWTs.\n                In case the signer is specified, the request argument will be\n                ignored.\n            use_metadata_identity_endpoint (bool): Whether to use GCE metadata\n                identity endpoint. For backward compatibility the default value\n                is False. If set to True, ``token_uri``, ``additional_claims``,\n                ``service_account_email``, ``signer`` argument should not be set;\n                otherwise ValueError will be raised.\n            quota_project_id (Optional[str]): The project ID used for quota and\n                billing.\n\n        Raises:\n            ValueError:\n                If ``use_metadata_identity_endpoint`` is set to True, and one of\n                ``token_uri``, ``additional_claims``, ``service_account_email``,\n                 ``signer`` arguments is set.\n        """
        super(IDTokenCredentials, self).__init__()
        self._quota_project_id = quota_project_id
        self._use_metadata_identity_endpoint = use_metadata_identity_endpoint
        self._target_audience = target_audience
        if use_metadata_identity_endpoint:
            if token_uri or additional_claims or service_account_email or signer:
                raise exceptions.MalformedError('If use_metadata_identity_endpoint is set, token_uri, additional_claims, service_account_email, signer arguments must not be set')
            else:
                self._token_uri = None
                self._additional_claims = None
                self._signer = None
        if service_account_email is None:
            sa_info = _metadata.get_service_account_info(request)
            self._service_account_email = sa_info['email']
        else:
            self._service_account_email = service_account_email
        if not use_metadata_identity_endpoint:
            if signer is None:
                signer = iam.Signer(request=request, credentials=Credentials(), service_account_email=self._service_account_email)
            self._signer = signer
            self._token_uri = token_uri or _DEFAULT_TOKEN_URI
            if additional_claims is not None:
                self._additional_claims = additional_claims
            else:
                self._additional_claims = {}
    def with_target_audience(self, target_audience):
        """Create a copy of these credentials with the specified target\n        audience.\n        Args:\n            target_audience (str): The intended audience for these credentials,\n            used when requesting the ID Token.\n        Returns:\n            google.auth.service_account.IDTokenCredentials: A new credentials\n                instance.\n        """
        if self._use_metadata_identity_endpoint:
            return self.__class__(None, target_audience=target_audience, use_metadata_identity_endpoint=True, quota_project_id=self._quota_project_id)
        else:
            return self.__class__(None, service_account_email=self._service_account_email, token_uri=self._token_uri, target_audience=target_audience, additional_claims=self._additional_claims.copy(), signer=self.signer, use_metadata_identity_endpoint=False, quota_project_id=self._quota_project_id)
    @_helpers.copy_docstring(credentials.CredentialsWithQuotaProject)
    def with_quota_project(self, quota_project_id):
        if self._use_metadata_identity_endpoint:
            return self.__class__(None, target_audience=self._target_audience, use_metadata_identity_endpoint=True, quota_project_id=quota_project_id)
        else:
            return self.__class__(None, service_account_email=self._service_account_email, token_uri=self._token_uri, target_audience=self._target_audience, additional_claims=self._additional_claims.copy(), signer=self.signer, use_metadata_identity_endpoint=False, quota_project_id=quota_project_id)
    @_helpers.copy_docstring(credentials.CredentialsWithTokenUri)
    def with_token_uri(self, token_uri):
        if self._use_metadata_identity_endpoint:
            raise exceptions.MalformedError('If use_metadata_identity_endpoint is set, token_uri must not be set')
        else:
            return self.__class__(None, service_account_email=self._service_account_email, token_uri=token_uri, target_audience=self._target_audience, additional_claims=self._additional_claims.copy(), signer=self.signer, use_metadata_identity_endpoint=False, quota_project_id=self.quota_project_id)
    def _make_authorization_grant_assertion(self):
        """Create the OAuth 2.0 assertion.\n        This assertion is used during the OAuth 2.0 grant to acquire an\n        ID token.\n        Returns:\n            bytes: The authorization grant assertion.\n        """
        now = _helpers.utcnow()
        lifetime = datetime.timedelta(seconds=_DEFAULT_TOKEN_LIFETIME_SECS)
        expiry = now + lifetime
        payload = {'iat': _helpers.datetime_to_secs(now), 'exp': _helpers.datetime_to_secs(expiry), 'iss': self.service_account_email, 'aud': self._token_uri, 'target_audience': self._target_audience}
        payload.update(self._additional_claims)
        token = jwt.encode(self._signer, payload)
        return token
    def _call_metadata_identity_endpoint(self, request):
        """Request ID token from metadata identity endpoint.\n\n        Args:\n            request (google.auth.transport.Request): The object used to make\n                HTTP requests.\n\n        Returns:\n            Tuple[str, datetime.datetime]: The ID token and the expiry of the ID token.\n\n        Raises:\n            google.auth.exceptions.RefreshError: If the Compute Engine metadata\n                service can\'t be reached or if the instance has no credentials.\n            ValueError: If extracting expiry from the obtained ID token fails.\n        """
        try:
            path = 'instance/service-accounts/default/identity'
            params = {'audience': self._target_audience, 'format': 'full'}
            metrics_header = {metrics.API_CLIENT_HEADER: metrics.token_request_id_token_mds()}
            id_token = _metadata.get(request, path, params=params, headers=metrics_header)
        except exceptions.TransportError as caught_exc:
            new_exc = exceptions.RefreshError(caught_exc)
            raise new_exc from caught_exc
        _, payload, _, _ = jwt._unverified_decode(id_token)
        return (id_token, datetime.datetime.utcfromtimestamp(payload['exp']))
    def refresh(self, request):
        """Refreshes the ID token.\n\n        Args:\n            request (google.auth.transport.Request): The object used to make\n                HTTP requests.\n\n        Raises:\n            google.auth.exceptions.RefreshError: If the credentials could\n                not be refreshed.\n            ValueError: If extracting expiry from the obtained ID token fails.\n        """
        if self._use_metadata_identity_endpoint:
            self.token, self.expiry = self._call_metadata_identity_endpoint(request)
        else:
            assertion = self._make_authorization_grant_assertion()
            access_token, expiry, _ = _client.id_token_jwt_grant(request, self._token_uri, assertion)
            self.token = access_token
            self.expiry = expiry
    @property
    @_helpers.copy_docstring(credentials.Signing)
    def signer(self):
        return self._signer
    def sign_bytes(self, message):
        """Signs the given message.\n\n        Args:\n            message (bytes): The message to sign.\n\n        Returns:\n            bytes: The message\'s cryptographic signature.\n\n        Raises:\n            ValueError:\n                Signer is not available if metadata identity endpoint is used.\n        """
        if self._use_metadata_identity_endpoint:
            raise exceptions.InvalidOperation('Signer is not available if metadata identity endpoint is used')
        else:
            return self._signer.sign(message)
    @property
    def service_account_email(self):
        """The service account email."""
        return self._service_account_email
    @property
    def signer_email(self):
        return self._service_account_email