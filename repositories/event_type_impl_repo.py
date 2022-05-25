from exceptions.resource_not_found import ResourceNotFound
from models.event_type_model import EventTypeModel
from util.db_connection import connection


def _row(row):
    return EventTypeModel(event_type_id=row[0], event_type=row[1], coverage_percentage=row[2])


class EventTypeImplRepo:
    def get_event_type_id(self, event_id):
        sql = 'SELECT * from event_type where event_type_id=%s'
        cursor = connection.cursor()
        data = (event_id,)
        cursor.execute(sql, data)

        row = cursor.fetchone()
        if row:
            return _row(row)
        else:
            raise ResourceNotFound(f"event_id {event_id} Not Found")

    def all_event_type(self):
        sql = 'SELECT * from event_type'
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        event_list = [_row(row) for row in rows]

        return event_list


def _main():
    etr = EventTypeImplRepo()
    print(etr.all_event_type())
    print("_______")


if __name__ == '__main__':
    _main()
