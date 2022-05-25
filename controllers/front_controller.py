# entry point of application
from controllers import emp_controller, home_controller, reim_controller, event_type_controller


def route(app):
    emp_controller.route(app)
    home_controller.route(app)
    reim_controller.route(app)
    event_type_controller.route(app)
