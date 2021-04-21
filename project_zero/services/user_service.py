from daos.user_dao_impl import UserDAOImpl
from daos.user_dao_temp import UserDAOTemp
from time import time

from exceptions.resource_unavailable import ResourceUnavailable
# from models import user


class UserService:
    # user_dao = UserDAOTemp()
    user_dao = UserDAOImpl()

    @classmethod
    def create_user(cls, user):
        return cls.user_dao.create_user(user)

    @classmethod
    def all_user(cls):
        return cls.user_dao.all_user()

    @classmethod
    def get_user(cls, user_id):
        return cls.user_dao.get_user(user_id)

    @classmethod
    def update_user(cls, user):

        # check if id exist then through resourcenotfound
        return cls.user_dao.update_user(user)

    @classmethod
    def delete_user(cls, user_id):
        return cls.user_dao.delete_user(user_id)

# -----------------------------------------------------------------------

    # @classmethod
    # def create_account(cls, account):
    #     return cls.user_dao.create_acoount(account)
    #
    # @classmethod
    # def all_account(cls):
    #     return cls.user_dao.all_account()

    # @classmethod
    # def create_user_withid(cls, user_id):
    #     user_exist = cls.user_dao.get_user(user_id)
    #     if user_exist:
    #         return cls.user_dao.create_user(user)
    # print("successfully created an account with another ID")

# @classmethod
# def checkout_movie(cls, user_id):
#     movie = cls.user_dao.get_user(user_id)
#     if movie.available:
#         movie.available = False
#         movie.return_date = int(time() + 604800)
#         cls.update_user(user)
#         return user.title
#     else:
#         raise ResourceUnavailable(f"Movie is checked out. Expected return: {movie.return_date}")

# @classmethod
# def checkin_movie(cls, movie_id):
#     movie = cls.movie_dao.get_movie(movie_id)
#     if not movie.available:
#         movie.available = True
#         movie.return_date = 0
#         cls.update_movie(movie)
#         return movie.title
#     else:
#         raise ResourceUnavailable(f"Movie is not checked out. Cannot be checked in.")
