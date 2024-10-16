from interface import IObserverBase

from dataclasses import dataclass


@dataclass
class Subject:
    """Субъект"""

    _data = None
    _observers = set()

    def attach(self, observer: IObserverBase):
        """Подписаться на оповещение"""
        if not isinstance(observer, IObserverBase):
            raise TypeError("Observer должен быть экземпляром ObserverBase")
        self._observers.add(observer)

    def detach(self, observer: IObserverBase):
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data: str):
        self._data = data
        self.notify(data)

    def notify(self, data: object):
        """Уведомить всех наблюдателей о событии"""
        for observer in self._observers:
            observer.update(data)
