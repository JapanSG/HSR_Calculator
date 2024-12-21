"""event"""


class Event:
    def __init__(self, observer) -> None:
        self.observer = observer

    def send(self):
        pass


class DamageEvent(Event):

    def send(self, char, target, damage, num):
        self.observer.notify([DamageEvent, char, target, damage, num])


class CritEvent(Event):

    def send(self, char, target):
        self.observer.notify([CritEvent, char, target])


class Relic2pcPassive(Event):

    def send(self, char, relic):
        self.observer.notify([Relic2pcPassive, char, relic])


class Relic4pcPassive(Event):

    def send(self, char, relic):
        self.observer.notify([Relic4pcPassive, char, relic])


class EventManager:
    def __init__(self) -> None:
        self._subscribers = []

    def attach(self, subscriber) -> None:
        self._subscribers.append(subscriber)

    def notify(self, event: list) -> None:
        for subscriber in self._subscribers:
            subscriber.update(event)


if __name__ == "__main__":
    print(Event == type(Event(987)))
