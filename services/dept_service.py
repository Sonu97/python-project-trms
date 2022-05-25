from repositories.dept_repo_impl import DeptRepoImpl


class DepartmentService:
    def __init__(self, dept_repo):
        self.dept_repo = dept_repo

    def get_dept_id(self, dept_id):
        return self.dept_repo.get_dept_id(dept_id)

    def all_dept(self):
        return self.dept_repo.all_dept()

    def update_dept(self, update):
        return self.dept_repo.update_dept(update)


class DeptRepo:
    pass


def _main():
    global ds
    dr: DeptRepoImpl = DeptRepoImpl()
    ds = DepartmentService(dr)
    print(ds.get_dept_id)
