from abc import ABC, abstractmethod


class IObserverBase(ABC):

    @abstractmethod
    def update(self, data: object):
        raise NotImplementedError()
