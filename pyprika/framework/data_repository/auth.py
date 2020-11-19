from abc import ABC, abstractmethod

HEADER_AUTHORIZATION = 'Authorization'

AUTH_BASIC = 'basic'
AUTH_DIGEST = 'digest'
AUTH_BEARER = 'bearer'
AUTH_OAUTH = 'oauth'

VALID_AUTH_TYPES = [
    AUTH_BASIC,
    AUTH_DIGEST,
    AUTH_BEARER,
    AUTH_OAUTH
]


class Auth(ABC):
    """Authentication container."""

    AUTH_TYPE = None

    def __init__(self):
        """Initialize authentication data."""
        return

    @abstractmethod
    def _get_authorize_header_value(self):
        """Calculate the value of the authorize header."""
        pass

    @property
    def auth_header(self):
        """Get the header value for this authentication type."""
        return {
            HEADER_AUTHORIZATION: str(self._get_authorize_header_value())
        }
