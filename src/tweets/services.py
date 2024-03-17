from sqlalchemy.ext.asyncio.session import AsyncSession
from tweets.schemas import TweetIn
from tweets.models import Tweet


async def create_tweet(
        tweet_in: TweetIn,
        session: AsyncSession
    ) -> Tweet:
    """New tweet creation"""
    tweet = Tweet(text=tweet_in.tweet_data)
    
    session.add(tweet)
    await session.commit()
    
    return tweet

