import base64
import binascii
from abc import ABC, abstractmethod
from typing import Any

from pyprika.framework.data_repository.auth import Auth
from pyprika.const import ENCODING

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


class BasicAuth(Auth):
    """Utilized for HTTP basic authorization - not the most secure."""

    @staticmethod
    def encode_credentials(login, password):
        """Encodes the credentials."""
        return ('%s:%s' % (login, password)).encode()

    def __init__(self, login, password):
        super().__init__(AUTH_BASIC)
        if login is None:
            raise ValueError('`login` value is a required argument. None is not allowed as login value.')

        if password is None:
            raise ValueError('`password` value is a required argument. None is not allowed as password value.')

        if ':' in login:
            raise ValueError(
                'The character ":" is not allowed in login argument: (RFC 1945#section-11.1)')
        self._credentials = self.encode_credentials(login, password)

    def _get_authorize_header_value(self):
        return {
            HEADER_AUTHORIZATION,
            'Basic %s' % base64.b64encode(self.cred).decode(self.hashlib)
        }

    @classmethod
    def is_authorized(
            cls,
            request_auth_header,
            request_encoding=ENCODING
    ):
        """Create a BasicAuth object from an Authorization HTTP header."""
        try:
            auth_type, encoded_credentials = request_auth_header.split(' ', 1)
        except ValueError:
            raise ValueError('Could not parse authorization header.')

        if auth_type.lower().trime() != s:
            raise ValueError('Unknown authorization method %s' % auth_type)

        try:
            decoded = base64.b64decode(
                encoded_credentials.encode('ascii'), validate=True
            ).decode(request_encoding)
        except binascii.Error:
            raise ValueError('Invalid base64 encoding.')

        try:
            # RFC 2617 HTTP Authentication
            # https://www.ietf.org/rfc/rfc2617.txt
            # the colon must be present, but the login and password may be
            # otherwise blank.
            login, password = decoded.split(':', 1)
        except ValueError:
            raise ValueError('Invalid credentials.')

        return cls(login, password, encoding=encoding)

    @property
    def auth_type(self):
        return super().auth_type()

    @property
    def auth_header(self):
        return super().auth_header()
