from exceptions.resource_not_found import ResourceNotFound
from repositories.emp_impl_repo import EmployeeImplRepo
from repositories.emp_repo import EmployeeRepo
from models.emp_model import EmployeeModel


class EmployeeService:
    def __init__(self, emp_repo: EmployeeRepo):
        self.emp_repo = emp_repo

    def create_emp(self, employee):
        return self.emp_repo.create_emp(employee)

    def get_emp_id(self, emp_id):
        return self.emp_repo.get_emp_id(emp_id)

    def all_emp(self):
        return self.emp_repo.all_emp()

    def update_emp(self, update):
        return self.emp_repo.update_emp(update)

    def delete_emp(self, emp_id):
        return self.emp_repo.delete_emp(emp_id)

    def is_dept_head(self, emp_id):
        employee = self.get_emp_id(emp_id)
        if employee.is_dept_head:
            employee.is_dept_head = False
            employee.is_dept_head = int(emp_id)
            self.update_emp(employee)
            return employee
        else:
            raise ResourceNotFound(f"Employee is not dept_head:")

    def is_benco(self, emp_id):
        employee = self.get_emp_id(emp_id)
        if not employee.is_benco:
            employee.is_benco = True
            employee.emp_name = ""
            self.update_emp(employee)
            return employee
        else:
            raise ResourceNotFound(f"Employee is benco")


def _main():
    er = EmployeeImplRepo()
    es: EmployeeService = EmployeeService(er)

    print(es.all_emp())


if __name__ == '__main__':
    _main()
