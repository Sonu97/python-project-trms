from abc import ABC, abstractmethod


class ReimFormRepo(ABC):
    @abstractmethod
    def create_reim_form(self, reim):
        pass

    # @abstractmethod
    # def get_reim_by_emp_id(self, emp_id, year):
    #     pass

    @abstractmethod
    def get_all_reim(self):
        pass

    @abstractmethod
    def get_all_reim_by_id(self, reim_form_id):
        pass

    @abstractmethod
    def update_received_grade(self, emp_id, reim_form_id):
        pass

    # @abstractmethod
    # def update_benco_reim_changed_amount(self, emp_id, reim_for_id):
    #     pass

    @abstractmethod
    def update_supervisor_confirmed(self, emp_id, reim_form_id):
        pass

    @abstractmethod
    def update_benco_confirmed(self, emp_id, reim_form_id):
        pass

    # @abstractmethod
    # def update_reim_form(self, reim_form_id):
    #     pass

    # @abstractmethod
    # def delete_reim_form(self, reim_form_id):
    #     pass

    # @abstractmethod
    # def get_total_reim_form(self):
    #     pass

    # @abstractmethod
    # def get_pending_reim(self):
    #     pass

    # @abstractmethod
    # def get_approved_reim(self):
    #     pass

    # @abstractmethod
    # def get_denied_reim(self):
    #     pass
    def get_reim_by_emp_id(self, emp_id, year):
        pass