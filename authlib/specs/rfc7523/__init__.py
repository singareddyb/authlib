# -*- coding: utf-8 -*-
"""
    authlib.specs.rfc7523
    ~~~~~~~~~~~~~~~~~~~~~

    This module represents a direct implementation of
    JSON Web Token (JWT) Profile for OAuth 2.0 Client
    Authentication and Authorization Grants.

    https://tools.ietf.org/html/rfc7523
"""

from .grant import JWTBearerGrant
from .client import (
    JWTBearerClientAssertion,
    client_secret_jwt_sign,
    private_key_jwt_sign,
)
