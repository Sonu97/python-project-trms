class EventTypeModel:
    def __init__(self, event_type_id=1, event_type="", coverage_percentage=1):
        self.event_type_id = event_type_id
        self.event_type = event_type
        self.coverage_percentage = coverage_percentage

    def __repr__(self):
        return str({
            'event_type_id': self.event_type_id,
            'event_type': self.event_type,
            'coverage_percentage': self.coverage_percentage,

        })

    def json(self):
        return {
            'eventTypeId': self.event_type_id,
            'eventType': self.event_type,
            'coveragePercentage': self.coverage_percentage,
        }


