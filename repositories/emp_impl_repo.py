import psycopg2
from exceptions.resource_not_found import ResourceNotFound
from models.emp_model import EmployeeModel
from util.db_connection import connection
from repositories.emp_repo import EmployeeRepo


def _row(row):
    # if row:
    return EmployeeModel(emp_id=row[0], emp_password=row[1], emp_name=row[2], emp_email=row[3],
                         supervisor_emp_id=row[4], is_dept_head=row[5], is_benco=row[6], is_admin=row[7],
                         dept_id=row[8])


# else:
#     return None


class EmployeeImplRepo:

    def create_emp(self, employee):
        sql = "INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"
        cursor = connection.cursor()

        cursor.execute(sql, [employee.emp_id, employee.emp_password, employee.emp_name, employee.emp_email,
                             employee.supervisor_emp_id, employee.is_dept_head, employee.is_benco,
                             employee.is_admin, employee.dept_id])
        connection.commit()
        row = cursor.fetchone()
        return _row(row)

    def get_emp_id(self, emp_id):
        sql = 'SELECT * from employee where emp_id=%s'
        cursor = connection.cursor()
        data = (emp_id,)
        cursor.execute(sql, data)

        row = cursor.fetchone()
        if row:
            return _row(row)
        else:
            raise ResourceNotFound(f"Emp_id {emp_id} Not Found")

    def all_emp(self):
        sql = 'SELECT * from employee'
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        emp_list = [_row(row) for row in rows]

        return emp_list

    def update_emp(self, update: EmployeeModel) -> object:
        sql = 'UPDATE employee SET emp_password=%s, emp_name=%s, emp_email=%s, supervisor_emp_id=%s,' \
              'is_dept_head=%s,is_benco=%s,is_admin=%s,dept_id=%s WHERE emp_id=%s RETURNING * '

        cursor = connection.cursor()

        cursor.execute(sql, [update.emp_password, update.emp_name, update.emp_email,
                             update.supervisor_emp_id, update.is_dept_head, update.is_benco,
                             update.is_admin, update.dept_id, update.emp_id])

        connection.commit()
        row = cursor.fetchone()
        if row:
            return _row(row)
        else:
            raise ResourceNotFound(f"Emp_id {update.emp_id} Not Found")
         
    def delete_emp(self, emp_id):
        sql = "DELETE FROM employee WHERE emp_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        connection.commit()


def _main():
    er = EmployeeImplRepo()
    # employee = er.get_emp_id()
    # print(employee)

    print(er.all_emp())
    print("-------------")
    # employee.emp_name = "Richa Singha"
    # employee = er.update_emp(employee)
    # row = EmployeeModel(emp_id=4, emp_password="pass777", emp_name='Richa' 'Shet', emp_email='rich@email.com',
    #                     supervisor_emp_id=3, dept_id=2)
    # print(er.create_emp(row))
    print(er.all_emp())
    # employee.emp_id = '8'
    # employee.emp_password = "pass000"
    # employee.emp_name = "Richa Singh"
    # employee.emp_email = "richa@email.com"
    # employee.supervisor_emp_id = '3'
    # employee.is_dept_head = '0'
    # employee.is_site_admin = '1'
    # employee.dept_id = '3'
    # employee = er.update_emp(employee)
    # print(er.create_emp(employee))

    print("success added employee")
    print("updated")


if __name__ == '__main__':
    _main()


