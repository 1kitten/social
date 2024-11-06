from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from dependencies import get_user_by_api_key
from tweets.services import create_tweet, delete_tweet
from tweets.schemas import TweetIn, TweetOut, TweetsList
from tweets.models import Tweet
from database import db_helper
from tweets.dependencies import tweet_by_id


router = APIRouter(tags=["Tweets"])


@router.get("/", response_model=TweetsList)
def get_list_of_tweets(user=Depends(get_user_by_api_key)):
    pass


@router.post("/", response_model=TweetOut)
async def post_new_tweet(
    tweet_in: TweetIn,
    session: AsyncSession = Depends(db_helper.session_dependency),
    user=Depends(get_user_by_api_key),
):
    """Create new tweet"""
    return await create_tweet(tweet_in=tweet_in, session=session)


@router.delete("/{id}")
async def delete_tweet_by_id(
    tweet: Tweet = Depends(tweet_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
    user=Depends(get_user_by_api_key),
):
    await delete_tweet(session=session, tweet=tweet)
    return {"result": True}
