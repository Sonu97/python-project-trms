from repositories import reim_form_repo
from repositories.reim_form_impl_repo import ReimFormImplRepo
from repositories.reim_form_repo import ReimFormRepo


class ReimService:
    def __init__(self, reim_form_repo: ReimFormRepo):
        self.reim_form_repo = reim_form_repo

    def create_reim_form(self, emp_id, event_type_id):
        return self.reim_form_repo.create_reim_form(emp_id, event_type_id)

    def get_reim_by_emp_id(self, emp_id, year):
        return self.reim_form_repo.get_reim_by_emp_id(emp_id, year)

    def get_all_reim(self):
        return self.reim_form_repo.get_all_reim()

    def get_all_reim_by_id(self, reim_form_id):
        return self.reim_form_repo.get_all_reim_by_id()

    def update_received_grade(self, emp_id, reim_form_id):
        return self.reim_form_repo.update_received_grade(emp_id, reim_form_id)

    def update_benco_confirmed(self, emp_id, reim_form_id):
        return self.reim_form_repo.update_benco_confirmed(emp_id, reim_form_id)

    def update_supervisor_confirmed(self, emp_id, reim_form_id):
        return self.reim_form_repo.update_supervisor_confirmed(emp_id, reim_form_id)

    def update_reim_form(self, reim_form_id):
        return self.reim_form_repo.update_reim_form()

    def delete_reim_form(self, reim_form_id):
        return self.reim_form_repo.delete_reim_form()


def _main():
    rf = ReimFormImplRepo()
    rs = ReimService(rf)

    print(rs.get_reim_by_emp_id(5, 2022))


if __name__ == '__main__':
    _main()