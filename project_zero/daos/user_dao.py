from abc import abstractmethod, ABC


class UserDAO(ABC):

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def create_user_wid(self, user_id):
        pass

    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def all_user(self):
        pass

    @abstractmethod
    def update_user(self, change):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass



