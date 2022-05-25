from abc import ABC
from util.db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from models.dept_model import DepartmentModel
from repositories.depo_repo import Deptrepo


def _build_dept(dept_data):
    if dept_data:
        return DepartmentModel(dept_id=dept_data[0], dept_name=dept_data[1])


class DeptRepoImpl(Deptrepo, ABC):
    def get_dept_id(self, dept_id):
        sql = "SELECT * FROM department WHERE dept_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [dept_id])
        dept_data = cursor.fetchone()

        if dept_data:
            return _build_dept(self.get_dept_id(dept_id))
        else:
            raise ResourceNotFound(f"Department ID not found")

    def all_dept(self):
        sql = "SELECT * FROM department"
        cursor = connection.cursor()
        cursor.execute(sql)

        dept_datas = cursor.fetchall()

        dept_list = [_build_dept(dept_data) for dept_data in dept_datas]

        return dept_list

    def update_dept(self, update):
        sql = "UPDATE department SET dept_id=%s, dept_name=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [update.dept_id, update.dept_name])

        connection.commit()
        dept_data = cursor.fetchone()

        return _build_dept(dept_data)


def _main():
    dr = DeptRepoImpl()
    dept = dr.get_dept_id(2)
    print(dept)

    print(dr.all_dept())


if __name__ == '__main__':
    _main()
