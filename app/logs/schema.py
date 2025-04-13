from datetime import datetime

from pydantic import BaseModel


class LogResponseSchema(BaseModel):
    id: int
    timestamp: datetime
    level: str
    tag: str
    message: str

    class Config:
        orm_mode = True
