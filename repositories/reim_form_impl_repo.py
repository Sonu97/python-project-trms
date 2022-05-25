from abc import ABC

from exceptions.resource_not_found import ResourceNotFound
from models.reimbursement_form_model import ReimbursementFormModel
from repositories.reim_form_repo import ReimFormRepo
from util.db_connection import connection


def _reim_form(record):
    # if record:
    print(len(record))
    return ReimbursementFormModel(reim_form_id=record[0], emp_id=record[1], event_type_id=record[2],
                                  event_start_date=record[3], event_end_date=record[4],
                                  event_cost=record[5], grading_format_id=record[6],
                                  passing_grade_cutoff=record[7],
                                  emp_form_submitted_date=record[8], received_grade=record[9],
                                  benco_reim_changed_amount=record[10],
                                  benco_reim_changed_date=record[11],
                                  emp_reim_cancelled_date=record[12],
                                  supervisor_presentation_confirmed_date=record[13],
                                  benco_grade_confirmed_date=record[14],
                                  is_amount_awarded=record[15])


# else:
#     return None


class ReimFormImplRepo:

    def create_reim_form(self, reim):
        sql = 'INSERT INTO reimbursement_form VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING*'

        cursor = connection.cursor()
        cursor.execute(sql, [reim.reim_form_id,
                             reim.emp_id,
                             reim.event_type_id,
                             reim.event_start_date,
                             reim.event_end_date,

                             reim.event_cost,
                             reim.grading_format_id,
                             reim.passing_grade_cutoff,
                             reim.emp_form_submitted_date,
                             reim.received_grade,
                             reim.benco_reim_changed_amount,
                             reim.benco_reim_changed_date,
                             reim.emp_reim_cancelled_date,
                             reim.supervisor_presentation_confirmed_date,
                             reim.benco_grade_confirmed_date,
                             reim.is_amount_awarded])

        connection.commit()
        record = cursor.fetchone()

        return _reim_form(record)

    def get_reim_by_emp_id(self, emp_id):
        sql = 'SELECT * FROM reimbursement_form WHERE emp_id = %s'  # AND year=%s
        cursor = connection.cursor()
        for emp_id in range(1):
            print("emp_id")

        assert isinstance(cursor, object)
        record = cursor.execute(sql, [emp_id])
        for emp_id in range(1):
            if record:
                return _reim_form(record)
        else:
            raise ResourceNotFound(f"Not found: {emp_id}")

    def get_total_amount_by_emp_id_year(self, emp_id, year):
        sql = 'SELECT SUM(event_cost) FROM reimbursement_form WHERE emp_id=%s and  extract(year from ' \
              'emp_form_submitted_date) = %s '
        cursor = connection.cursor()
        cursor.execute(sql, emp_id, year)
        record = cursor.fetchone()

        if record:
            return _reim_form(record)
        else:
            raise ResourceNotFound(f"Not found: {emp_id} {year}")

    def get_details_by_year(self, year):
        sql = 'SELECT * FROM reimbursement_form WHERE extract(year from emp_form_submitted_date) = %s'
        cursor = connection.cursor()
        cursor.execute(sql, year)
        record = cursor.fetchone()

        if record:
            return _reim_form(record)
        else:
            raise ResourceNotFound(f"Not found:  {year}")

    def get_all_reim(self):
        sql = "SELECT * FROM reimbursement_form"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        reim_list = [_reim_form(record) for record in records]
        # reim_list = [ ReimbursementFormModel() ]

        return reim_list

    def update_received_grade(self, emp_id, reim_form_id):
        sql = "UPDATE reimbursement_form SET reim_form_id=%s, emp_id=%s, event_type_id=%s," \
              "event_start_date=%s, event_end_date=%s," \
              " event_cost=%s, grading_format_id=%s," \
              "passing_grade_cutoff=%s," \
              "emp_form_submitted_date=%s, received_grade=%s," \
              "benco_reim_changed_amount=%s," \
              "benco_reim_changed_date=%s," \
              "emp_reim_cancelled_date=%s," \
              "supervisor_presentation_confirmed_date=%s," \
              "benco_grade_confirmed_date=%s, is_amount_awarded=%s" \
              "RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, emp_id, reim_form_id)
        connection.commit()
        record = cursor.fetchone()

        return _reim_form(record)

    def update_benco_confirmed(self, emp_id, reim_form_id):
        sql = "UPDATE reimbursement_form SET reim_form_id=%s, emp_id=%s, event_type_id=%s," \
              "event_start_date=%s, event_end_date=%s," \
              "event_description=%s, event_cost=%s, grading_format_id=%s," \
              "passing_grade_cutoff=%s," \
              "emp_form_submitted_date=%s, received_grade=%s," \
              "benco_reim_changed_amount=%s," \
              "benco_reim_changed_date=%s," \
              "emp_reim_cancelled_date=%s," \
              "supervisor_presentation_confirmed_date=%s," \
              "benco_grade_confirmed_date=%s, is_amount_awarded=%s" \
              "RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, emp_id, reim_form_id)
        connection.commit()
        record = cursor.fetchone()

        return _reim_form(record)

    def update_supervisor_confirmed(self, emp_id, reim_form_id):
        sql = "UPDATE reimbursement_form SET reim_form_id=%s, emp_id=%s, event_type_id=%s," \
              "event_start_date=%s, event_end_date=%s," \
              "event_description=%s, event_cost=%s, grading_format_id=%s," \
              "passing_grade_cutoff=%s," \
              "emp_form_submitted_date=%s, received_grade=%s," \
              "benco_reim_changed_amount=%s," \
              "benco_reim_changed_date=%s," \
              "emp_reim_cancelled_date=%s," \
              "supervisor_presentation_confirmed_date=%s," \
              "benco_grade_confirmed_date=%s, is_amount_awarded=%s" \
              "RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, emp_id, reim_form_id)
        connection.commit()
        record = cursor.fetchone()

        return _reim_form(record)

    def update_benco_rein_changed_amount(self, emp_id, reim_form_id):
        sql = "UPDATE reimbursement_form SET reim_form_id=%s, emp_id=%s, event_type_id=%s," \
              "event_start_date=%s, event_end_date=%s," \
              "event_description=%s, event_cost=%s, grading_format_id=%s," \
              "passing_grade_cutoff=%s," \
              "emp_form_submitted_date=%s, received_grade=%s," \
              "benco_reim_changed_amount=%s," \
              "benco_reim_changed_date=%s," \
              "emp_reim_cancelled_date=%s," \
              "supervisor_presentation_confirmed_date=%s," \
              "benco_grade_confirmed_date=%s, is_amount_awarded=%s" \
              "RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, emp_id, reim_form_id)
        connection.commit()
        record = cursor.fetchone()

        return _reim_form(record)


def _main():
    rf = ReimFormImplRepo()
    print(rf.get_all_reim())
    print("-----------------")
    if True:
        reim = rf.get_reim_by_emp_id(emp_id=1)
        return reim

#     print("-----w-i-p-------")
#
#     reim = ReimbursementFormModel(emp_id=7, event_type_id=2)
#     reim = rf.create_reim_form(reim, 2)
#
#
# if __name__ == '__main__':
#     _main()
