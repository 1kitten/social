from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from dependencies import get_user_by_api_key
from tweets.services import create_tweet
from tweets.schemas import TweetIn, TweetOut
from database import db_helper


router = APIRouter(tags=["Tweets"])


@router.post("/", response_model=TweetOut)
async def post_new_tweet(
        tweet_in: TweetIn,
        session: AsyncSession = Depends(db_helper.session_dependency),
        user = Depends(get_user_by_api_key)
    ):
    """Create new tweet"""
    return await create_tweet(tweet_in=tweet_in, session=session)

