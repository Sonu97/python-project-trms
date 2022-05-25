class GradingFormatModel:
    def __init__(self, grading_format_id=0, grading_format="", grade=""):
        self.grading_format_id = grading_format_id
        self.grading_format = grading_format
        self.grade = grade

    def __repr__(self):
        return str({
            'grading_format_id': self.grading_format_id,
            'grading_format': self.grading_format,
            'grade': self.grade,
        })

    def json(self):
        return {
            'grading_format_id': self.grading_format_id,
            'grading_format': self.grading_format,
            'grade': self.grade,
        }
