from sqlalchemy.ext.asyncio.session import AsyncSession
from tweets.schemas import TweetIn
from tweets.models import Tweet


async def create_tweet(tweet_in: TweetIn, session: AsyncSession) -> Tweet:
    """New tweet creation"""
    tweet = Tweet(text=tweet_in.tweet_data)

    session.add(tweet)
    await session.commit()

    return tweet


async def get_tweet(session: AsyncSession, tweet_id: int) -> Tweet:
    return await session.get(Tweet, tweet_id)


async def delete_tweet(session: AsyncSession, tweet: Tweet) -> None:
    await session.delete(tweet)
    await session.commit()
