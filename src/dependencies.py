from typing import Annotated
from exceptions import ApiKeyNotFoundError
from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

api_key = APIKeyHeader(name="api-key", auto_error=False)


async def get_user_by_api_key(
        api_key: Annotated[str, Security(api_key)]
    ):
    """Getting user by api-key from headers"""
    if not api_key:
        raise ApiKeyNotFoundError("Bad api-key")

    #TODO: User check by session
    #user = session
    #return user

