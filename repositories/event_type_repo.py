from abc import ABC, abstractmethod


class EventTypeRepo(ABC):

    @abstractmethod
    def get_event_type_id(self, event_id):
        pass

    @abstractmethod
    def all_event_type(self):
        pass
