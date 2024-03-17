from typing import Annotated
from pydantic import BaseModel, ConfigDict
from annotated_types import MaxLen, MinLen


class TweetIn(BaseModel):
    """Schema for new tweet"""
    tweet_data: Annotated[str, MinLen(1), MaxLen(500)]
    tweet_media_ids: list[int] = []


class TweetOut(BaseModel):
    """Scheme for tweet after creation"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    result: bool = True
