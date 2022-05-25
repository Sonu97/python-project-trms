from abc import ABC, abstractmethod


class EmployeeRepo(ABC):
    @abstractmethod
    def create_emp(self, emp):
        pass

    @abstractmethod
    def get_emp_id(self, emp_id):
        pass

    @abstractmethod
    def all_emp(self):
        pass

    @abstractmethod
    def update_emp(self, update):
        pass

    @abstractmethod
    def delete_emp(self, emp_id):
        pass
