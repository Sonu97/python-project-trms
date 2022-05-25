from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models import event_type_model
from models.event_type_model import EventTypeModel
from repositories.event_type_impl_repo import EventTypeImplRepo
from services.event_service import EventService

etr = EventTypeImplRepo()
ets = EventService(etr)


# def _row(row):
#     EventTypeModel(event_type_id=row[0], event_type=row[1], coverage_percentage=row[2])


def route(app):
    @app.route("/events", methods=['GET'])
    def all_event_type():
        return jsonify([event_type_model.json() for event_type_model in ets.all_event_type()])

    @app.route("/events/event_id", methods=['GET'])
    def get_event_type_id(event_id):
        try:
            return ets.get_event_type_id(int(event_id)).json(), 200
        except ValueError as e:
            return "Not Valid Id", 400
        except ResourceNotFound as r:
            return r.message, 404
