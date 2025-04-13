from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.logs import service
from app.logs.schema import LogResponseSchema
from core.database import get_db

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/", response_model=List[LogResponseSchema])
def get_logs(
    # TODO
    db: Session = Depends(get_db),
):
    return service.get_logs(db)
