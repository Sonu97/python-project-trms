from repositories.event_type_impl_repo import EventTypeImplRepo
from repositories.event_type_repo import EventTypeRepo
from models.event_type_model import EventTypeModel


class EventService:
    def __init__(self, event_type_repo: EventTypeRepo):
        self.event_type_repo = event_type_repo

    def get_event_type_id(self, event_id):
        return self.event_type_repo.get_event_type_id(event_id)

    def all_event_type(self):
        return self.event_type_repo.all_event_type()


# def _main():
#     etr = EventTypeImplRepo()
#     ets: EventService = EventService(etr)
#
#     print(ets.all_event_type())
#
#
# if __name__ == '__main__':
#     _main()
