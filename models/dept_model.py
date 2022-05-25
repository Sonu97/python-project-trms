class DepartmentModel:
    def __init__(self, dept_id=0, dept_name=""):
        self.dept_id = dept_id
        self.dept_name = dept_name

    def __repr__(self):
        return ({
            'dept_id': self.dept_id,
            'dept_name': self.dept_name,

        })
