import flask
from flask import request, jsonify, render_template, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from exceptions.resource_not_found import ResourceNotFound
from models.emp_model import EmployeeModel
from repositories.emp_impl_repo import EmployeeImplRepo
from services.emp_service import EmployeeService

er = EmployeeImplRepo()
es = EmployeeService(er)


def route(app):
    @app.route("/employees", methods=['GET'])
    def all_emp():
        return jsonify([employee.json() for employee in es.all_emp()])

    @app.route("/employees/<emp_id>", methods=['GET'])
    def get_emp_id(emp_id):
        try:
            return es.get_emp_id(int(emp_id)).json(), 200
        except ValueError as e:
            return "Not Valid Id", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees", methods=["POST"])
    def create_emp():
        body = request.json
        employee = EmployeeModel(emp_id=body["empId"], emp_password=body["empPassword"], emp_name=body["empName"],
                                 emp_email=body["empEmail"], supervisor_emp_id=body["supervisorEmpId"],
                                 is_dept_head=body["isDeptHead"], is_benco=body["isBenco"], is_admin=body["isAdmin"],
                                 dept_id=body["deptId"])

        employee = es.create_emp(employee)
        response = flask.Response(employee)
        response.headers['Content-Type'] = 'application/json'
        return response

        # return request.json

    @app.route("/employees/<emp_id>", methods=["PUT"])
    def put_emp(emp_id):
        body = request.json
        employee = EmployeeModel(emp_id=int(emp_id), emp_password=body["empPassword"], emp_name=body["empName"],
                                 emp_email=body["empEmail"], supervisor_emp_id=body["supervisorEmpId"])

        employee = es.update_emp(employee)
        # return "employee updated"

        if isinstance(employee, str):
            return employee, 404
        else:
            return employee.json()

    @app.route("/employees/<emp_id>", methods=["DELETE"])
    def delete_emp(emp_id):
        es.delete_emp(emp_id)
        return '', 204

    # @app.route("/employees/<emp_id>", methods=["PATCH"])
    # def patch_emp(emp_id):
    #    action = request.json['action']
    #
    # # if action == "is_dept_head" or action == "is_benco": #      try: #          employee = es.is_dept_head(int(
    # emp_id)) if action == "is_dept_head" else es.is_benco(int(emp_id)) #          return f"Employee is Dept Head{
    # 'Emp_is_Dept_head' if action == 'is_dept_head' else 'is_benco' } employee:{employee.emp_name}" except
    # ValueError: return "Not a Valid ID", 400 else: abort(400, "Body must contain a JSON with an result property and
    # a value of 'is_dept_head' or 'is_benco'") print(action)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for('http://localhost:5000'))
        return render_template('login.html', error=error)
