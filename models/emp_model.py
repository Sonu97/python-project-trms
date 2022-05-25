class EmployeeModel:
    def __init__(self, emp_id=0, emp_password="", emp_name="", emp_email="", supervisor_emp_id=0, is_dept_head=0,
                 is_benco=0,
                 is_admin=0, dept_id=0):
        self.emp_id = emp_id
        self.emp_password = emp_password
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.supervisor_emp_id = supervisor_emp_id
        self.is_dept_head = is_dept_head
        self.is_benco = is_benco
        self.is_admin = is_admin
        self.dept_id = dept_id

    def __repr__(self):
        return ({
            'emp_id': self.emp_id,
            'emp_password': self.emp_password,
            'emp_name': self.emp_name,
            'emp_email': self.emp_email,
            'supervisor_emp_id': self.supervisor_emp_id,
            'is_dept_head': self.is_dept_head,
            'is_benco': self.is_benco,
            'is_admin': self.is_admin,
            'dept_id': self.dept_id,

        })

    def json(self):
        return {
            'empId': self.emp_id,
            'empPassword': self.emp_password,
            'empName': self.emp_name,
            'empEmail': self.emp_email,
            'supervisorEmpId': self.supervisor_emp_id,
            'isDeptHead': self.is_dept_head,
            'isBenco': self.is_benco,
            'isAdmin': self.is_admin,
            'deptId': self.dept_id,

        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, EmployeeModel):
            return False

        return self.__dict__ == other.__dict__


def _main():
    emp1 = EmployeeModel()
    emp1 = EmployeeModel(emp_id=7, emp_password='apple', emp_name='Tina P', emp_email='t@yahoo.com',
                         supervisor_emp_id=2, is_dept_head=0, is_benco=0, is_admin=0, dept_id=5)
    print(emp1)


if __name__ == '__main__':
    _main()
