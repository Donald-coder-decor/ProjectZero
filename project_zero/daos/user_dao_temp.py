from daos.user_dao import UserDAO
from exceptions.resource_not_found import ResourceNotFound
from models import user
from util.temp_db import TempDB as db


class UserDAOTemp(UserDAO):

    def create_user(self, user):
        db.users[user.user_id] = user

    def create_user_withid(self, user_id):
        db.users[user.user_id] = user

    def get_user(self, user_id):
        try:
            return db.users[user_id]
        except KeyError:
            raise ResourceNotFound(f"User with id: {user_id} - Not Found")

    def all_user(self):

        return [user.json() for user in db.users.values()]

    def update_user(self, change):
        db.users.update({change.user_id: change})

    def delete_user(self, user_id):
        del db.users[user_id]
