from datetime import datetime

from sqlalchemy.orm import Session

from core.models import Log


def get_logs(
    start: datetime | None,
    end: datetime | None,
    level: str | None,
    tag: str | None,
    db: Session,
) -> list[Log]:
    query = db.query(Log)
    if start:
        query = query.filter(Log.timestamp >= start)
    if end:
        query = query.filter(Log.timestamp <= end)
    if level:
        query = query.filter(Log.level == level)
    if tag:
        query = query.filter(Log.tag == tag)
    return query.all()
