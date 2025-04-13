from sqlalchemy.orm import Session

from app.logs.schema import LogResponseSchema


def get_logs(db: Session) -> list[LogResponseSchema]:
    pass
