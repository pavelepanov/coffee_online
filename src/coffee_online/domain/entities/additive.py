from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.additive_id import AdditiveId
from coffee_online.domain.value_objects.additive_title import AdditiveTitle


class Additive(Entity):
    def __init__(self, id: AdditiveId, title: AdditiveTitle) -> None:
        super().__init__(id=id)
        self.title = title


def additive_factory(id: int, title: str) -> Additive:
    return Additive(
        id=AdditiveId(id),
        title=AdditiveTitle(title),
    )
