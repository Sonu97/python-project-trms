from abc import ABC, abstractmethod


class ApprovalsRepo(ABC):
    @abstractmethod
    def create_approvals(self, approvals):
        pass

    @abstractmethod
    def get_by_approval_id(self, approval_id):
        pass

    @abstractmethod
    def all_approvals(self):
        pass

    @abstractmethod
    def update_approvals(self, update):
        pass

    @abstractmethod
    def delete_approvals(self, approval_id):
        pass

