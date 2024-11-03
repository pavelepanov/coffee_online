from pydantic import BaseModel


class ProfileCreateSchema(BaseModel):
    name: str
    sex: str
    user_id: int
