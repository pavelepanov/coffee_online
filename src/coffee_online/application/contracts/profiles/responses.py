from dataclasses import dataclass


@dataclass(frozen=True)
class ProfileResponse:
    id: int
    name: str
    sex: str
    user_id: int
