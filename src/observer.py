from interface import IObserverBase

from dataclasses import dataclass


@dataclass
class Observer(IObserverBase):
    """Наблюдатель"""

    _name: str

    def update(self, data):
        print(f"{self._name}: {data}")

    def __hash__(self) -> int:
        return super().__hash__()
