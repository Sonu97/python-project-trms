from http import HTTPStatus

from flask import request, jsonify, render_template, url_for
from werkzeug.utils import redirect

from exceptions.resource_not_found import ResourceNotFound
from models.reimbursement_form_model import ReimbursementFormModel
from repositories.reim_form_impl_repo import ReimFormImplRepo
from services.reim_service import ReimService

rr = ReimFormImplRepo()
rs = ReimService(rr)


def route(app):
    @app.route("/reim_form", methods=['GET'])
    def get_all_reim():
        result = [reim_form.json() for reim_form in rs.get_all_reim()]
        print(result, type(result))
        return jsonify(result)

    @app.route("/view/reim", methods=['GET'])
    def get_all_reim_html():
        result = [reim_form.json() for reim_form in rs.get_all_reim()]
        keys = []
        if result is not None and len(result) > 0:
            keys = result[0].keys()
        print(result, type(result))
        return render_template(
            'view_all_reims.html',
            title="View all reimbursements",
            result=result, keys=keys
        )

    @app.route("/reim/<reim_id>", methods=['GET'])
    def get_all_reim_by_id(reim_id):
        try:
            return rs.get_all_reim_by_id(int(reim_id))
        except ValueError as e:
            return "Not Valid Id", HTTPStatus.BAD_REQUEST
        except ResourceNotFound as r:
            return r.message

    @app.route("/reim_form", methods=["POST"])
    def create_reim_form():
        body = request.json
        reim = ReimbursementFormModel(reim_form_id=body["reimFormId"], emp_id=body["empId"],
                                      event_type_id=body["eventTypeId"], event_start_date=body["eventStartDate"],
                                      event_end_date=body["eventEndDate"],
                                      event_cost=body["eventCost"],
                                      grading_format_id=body["gradingFormatId"],
                                      passing_grade_cutoff=body["passingGradeCutoff"],
                                      emp_form_submitted_date=body["empFormSubmittedDate"],
                                      received_grade=body["receivedGrade"],
                                      benco_reim_changed_amount=body["bencoReimChangedAmount"],
                                      benco_reim_changed_date=body["bencoReimChangedDate"],
                                      emp_reim_cancelled_date=body["empReimCancelledDate"],
                                      supervisor_presentation_confirmed_date=body[
                                          "supervisorPresentationConfirmedDate"],
                                      benco_grade_confirmed_date=body["bencoGradeConfirmedDate"],
                                      is_amount_awarded=body["isAmountAwarded"])
        reim = rs.create_reim_form(reim)

        return request.json()

    @app.route("/reim/<reim_id>", methods=["DELETE"])
    def delete_reim_form(reim_form_id):
        rs.delete_reim_form(reim_form_id)
        return '', 204

    @app.route("/add/reim", methods=["GET", "POST"])
    def add_reim():
        if request.method == 'GET':
            return render_template(
                'trms.html',
                title="Add reimbursements"
            )
        else:
            print(request.form["employeename"])
            print(request.form["reimformid"])
            print(request.form["empid"])
            reim = ReimbursementFormModel(reim_form_id=request.form["employeename"], emp_id=request.form["empId"])
            # event_type_id=body["eventTypeId"], event_start_date=body["eventStartDate"],
            # event_end_date=body["eventEndDate"],
            # event_cost=body["eventCost"],
            # grading_format_id=body["gradingFormatId"],
            # passing_grade_cutoff=body["passingGradeCutoff"],
            # emp_form_submitted_date=body["empFormSubmittedDate"],
            # received_grade=body["receivedGrade"],
            # benco_reim_changed_amount=body["bencoReimChangedAmount"],
            # benco_reim_changed_date=body["bencoReimChangedDate"],
            # emp_reim_cancelled_date=body["empReimCancelledDate"],
            # supervisor_presentation_confirmed_date=body[
            #     "supervisorPresentationConfirmedDate"],
            # benco_grade_confirmed_date=body["bencoGradeConfirmedDate"],
            # is_amount_awarded=body["isAmountAwarded"])
            # )
            # reim = rs.create_reim_form(reim)

            return redirect('/view/reim')
