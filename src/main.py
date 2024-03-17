from contextlib import asynccontextmanager
from fastapi import FastAPI
from exceptions import ApiKeyNotFoundError, NoUserFoundError
from exceptions_handlers import api_key_not_found_exception_handler, no_user_found_exception_handler
from tweets.router import router as tweets_router
import uvicorn
from database import db_helper, Base


@asynccontextmanager 
async def lifespan(app: FastAPI):
    """Create database tables on start up"""
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(title="twitter", lifespan=lifespan)
app.include_router(tweets_router, prefix="/api/tweets")

app.add_exception_handler(ApiKeyNotFoundError, api_key_not_found_exception_handler)
app.add_exception_handler(NoUserFoundError, no_user_found_exception_handler)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
