from abc import ABC,abstractmethod


class Deptrepo(ABC):
    @abstractmethod
    def get_dept_id(self, dept_id):
        pass

    @abstractmethod
    def all_dept(self):
        pass

    @abstractmethod
    def update_dept(self, update):
        pass
