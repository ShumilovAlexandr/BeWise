import datetime

from sqlalchemy import (Text,
                        DateTime,
                        Integer,
                        String,
                        ForeignKey)
from sqlalchemy.orm import (DeclarativeBase, 
                            Mapped, 
                            mapped_column)


class Base(DeclarativeBase):
    pass


class Quiz(Base):
    __tablename__ = "quiz"

    question_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_text: Mapped[str] = mapped_column(Text, unique=True)
    answer_text: Mapped[str] = mapped_column(Text, unique=True)
    create_date_time: Mapped[datetime.datetime] = mapped_column(DateTime)
