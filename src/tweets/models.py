from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from datetime import datetime


class Tweet(Base):
    """Tweets model"""
    __tablename__ = "tweets"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    is_removed: Mapped[bool] = mapped_column(nullable=False, default=False)
