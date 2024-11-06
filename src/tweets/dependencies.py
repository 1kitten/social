from fastapi import Path, Depends, status, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from database import db_helper
from tweets.models import Tweet
from tweets.services import get_tweet


async def tweet_by_id(
    tweet_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Tweet:
    tweet = await get_tweet(session=session, tweet_id=tweet_id)
    if tweet is not None:
        return tweet

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Tweet {tweet_id} not found."
    )
