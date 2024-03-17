from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from exceptions import ApiKeyNotFoundError, NoUserFoundError


async def api_key_not_found_exception_handler(_: Request, exc: ApiKeyNotFoundError):
    """Handler ApiKeyNotFoundError exception"""
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=jsonable_encoder(
            {"result": False, "message": f"{exc}. Secify api-key header!"}
        ),
    )


async def no_user_found_exception_handler(_: Request, exc: NoUserFoundError):
    """Handler NoUserFoundError exception"""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {"result": False, "message": f"{exc}. No user with that api-key found!"}
        ),
    )
