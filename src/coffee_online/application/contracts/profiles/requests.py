from dataclasses import dataclass


@dataclass(frozen=True)
class CreateProfileRequest:
    name: str
    sex: str
    user_id: int
