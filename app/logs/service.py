from datetime import datetime

from sqlalchemy.orm import Session

from app.logs import repository
from app.logs.schema import LogResponseSchema


def get_logs(
    start: datetime | None,
    end: datetime | None,
    level: str | None,
    tag: str | None,
    db: Session,
) -> list[LogResponseSchema]:
    return repository.get_logs(start, end, level, tag, db)
