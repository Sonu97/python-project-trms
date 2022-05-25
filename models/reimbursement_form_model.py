import datetime


class ReimbursementFormModel:
    def __init__(self, reim_form_id=1, emp_id=1, event_type_id=1, event_start_date=datetime, event_end_date=datetime,
                 event_cost=0, grading_format_id=1, passing_grade_cutoff=0,
                 emp_form_submitted_date=datetime, received_grade=0, benco_reim_changed_amount=0,
                 benco_reim_changed_date=datetime,
                 emp_reim_cancelled_date=datetime, supervisor_presentation_confirmed_date=datetime,
                 benco_grade_confirmed_date=datetime, is_amount_awarded=0):
        self.reim_form_id = reim_form_id
        self.emp_id = emp_id
        self.event_type_id = event_type_id
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date

        self.event_cost = event_cost
        self.grading_format_id = grading_format_id
        self.passing_grade_cutoff = passing_grade_cutoff
        self.emp_form_submitted_date = emp_form_submitted_date
        self.received_grade = received_grade
        self.benco_reim_changed_amount = benco_reim_changed_amount
        self.benco_reim_changed_date = benco_reim_changed_date
        self.emp_reim_cancelled_date = emp_reim_cancelled_date
        self.supervisor_presentation_confirmed_date = supervisor_presentation_confirmed_date
        self.benco_grade_confirmed_date = benco_grade_confirmed_date
        self.is_amount_awarded = is_amount_awarded

    def __repr__(self):
        return str({
            'reim_form_id': self.reim_form_id,
            'emp_id': self.emp_id,
            'event_type_id': self.event_type_id,
            'event_start_date': self.event_start_date,
            'event_end_date': self.event_end_date,

            'event_cost': self.event_cost,
            'grading_format_id': self.grading_format_id,
            'passing_grade_cutoff': self.passing_grade_cutoff,
            'emp_form_submitted_date': self.emp_form_submitted_date,
            'received_grade': self.received_grade,
            'benco_reim_changed_amount': self.benco_reim_changed_amount,
            'benco_reim_changed_date': self.benco_reim_changed_date,
            'emp_reim_cancelled_date': self.emp_reim_cancelled_date,
            'supervisor_presentation_confirmed_date': self.supervisor_presentation_confirmed_date,
            'benco_grade_confirmed_date': self.benco_grade_confirmed_date,
            'is_amount_awarded': self.is_amount_awarded,

        })

    def json(self):
        return {
            'reimFormId': self.reim_form_id,
            'empId': self.emp_id,
            'eventTypeId': self.event_type_id,
            'eventStartDate': self.event_start_date,
            'eventEndDate': self.event_end_date,

            'eventCost': self.event_cost,
            'gradingFormatId': self.grading_format_id,
            'passingGradeCutoff': self.passing_grade_cutoff,
            'empFormSubmittedDate': self.emp_form_submitted_date,
            'receivedGrade': self.received_grade,
            'bencoReimChangedAmount': self.benco_reim_changed_amount,
            'bencoReimChangedDate': self.benco_reim_changed_date,
            'empReimCancelledDate': self.emp_reim_cancelled_date,
            'supervisorPresentationConfirmedDate': self.supervisor_presentation_confirmed_date,
            'bencoGradeConfirmedDate': self.benco_grade_confirmed_date,
            'isAmountAwarded': self.is_amount_awarded,
        }
