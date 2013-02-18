from django.http import HttpResponseRedirect
from .http import HttpResponseUnauthorized


class InvalidRequest(Exception):
    error = "invalid_request"


class ClientNotProvided(InvalidRequest):
    reason = "The client was malformed or invalid"


class ClientDoesNotExist(InvalidRequest):
    reason = "The client was malformed or invalid."


class InvalidClient(Exception):
    error = "invalid_client"


class ClientSecretNotValid(InvalidClient):
    reason = "The client secret was malformed or invalid."


class InvalidGrant(Exception):
    error = "invalid_grant"


class RedirectUriNotProvided(InvalidRequest):
    reason = "The redirect URI was malformed or invalid."


class RedirectUriDoesNotValidate(InvalidRequest):
    reason = "The reidrect URI does not validate against the client host."


class InvalidScope(Exception):
    error = "invalid_scope"


class ScopeNotDefined(InvalidScope):
    reason = "The scope was malformed or invalid."


class ScopeNotValid(InvalidScope):
    reason = "The scope contained values which were incorrect."


class ResponseTypeNotDefined(InvalidRequest):
    reason = "The request type was malformed or invalid."


class ResponseTypeNotValid(Exception):
    error = "unsupported_response_type"
    reason = "The request type was malformed or invalid."


class AuthorizationCodeNotProvided(InvalidRequest):
    reason = "The authorization code was malformed or invalid."


class AuthorizationCodeNotValid(InvalidRequest):
    reason = "The authorization code was malformed or invalid."


class AuthorizationCodeAlreadyUsed(InvalidRequest):
    reason = "The authorization code was already used to get a refresh token."


class AccessDenied(Exception):
    error = "access_denied"


class AuthorizationDenied(AccessDenied):
    reason = "The request for permission was denied."