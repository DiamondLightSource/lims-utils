from dataclasses import dataclass
from typing import Optional
from fastapi import Request

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


@dataclass
class GenericUser:
    """Generic user model, to be used with ISPyB"""
    fedid: str
    id: str
    familyName: str
    title: str
    givenName: str
    permissions: list[str]

class CookieOrHTTPBearer(HTTPBearer):
    """Authentication model class that takes in cookies, and falls back to authorization bearer headers if 
    the cookie can't be found"""
    def __init__(
        self,
        *,
        bearerFormat: Optional[str] = None,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
        cookie_key: str = "cookie_auth"
    ):
        """:param str cookie_key: Cookie key to look for in requests
        
        Otherwise, extends FastAPIs HTTPBearer."""
        super().__init__(
            bearerFormat=bearerFormat,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )

        self.cookie_key = cookie_key

    async def __call__(self, request: Request):
        token = request.cookies.get(self.cookie_key)
        if token is not None:
            return HTTPAuthorizationCredentials(scheme="cookie", credentials=token)
        return await super().__call__(request)
