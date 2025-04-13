from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.logs import service
from app.logs.schema import LogResponseSchema
from core.database import get_db

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/", response_model=List[LogResponseSchema])
def get_logs(
    start: datetime | None = Query(None),
    end: datetime | None = Query(None),
    level: str | None = Query(None),
    tag: str | None = Query(None),
    db: Session = Depends(get_db),
):
    return service.get_logs(start, end, level, tag, db)
