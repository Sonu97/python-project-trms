from abc import ABC, abstractmethod


class GradingRepo(ABC):
    @abstractmethod
    def get_grading_by_id(self, emp_id):
        pass

    @abstractmethod
    def update_grade(self, emp_id, grading_format_id):
        pass

    @abstractmethod
    def update_grading(self,grading_format_id):
        pass

    @abstractmethod
    def get_all_grading(self):
        pass
