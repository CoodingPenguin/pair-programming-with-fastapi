from pydantic import BaseModel


class LogResponseSchema(BaseModel):
    # TODO

    class Config:
        orm_mode = True
