from flask import jsonify, request
from werkzeug.exceptions import abort

from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.account import Account
from models.user import User
# from models.account import Account
from services.account_service import AccountService
from services.user_service import UserService


# ---------------- Retrieve all users from the database and return status code of 200 for successful retrieval

def route(app):
    @app.route("/users", methods=['GET'])
    def get_all_user():
        return jsonify(UserService.all_user()), 200

    # ---------------- Retrieve user with a specific ID from the database and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/users/<user_id>", methods=['GET'])
    def get_user(user_id):
        try:
            user = UserService.get_user(int(user_id))
            return jsonify(user.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # +++++++++++++++++ Retrieve an account  with a specific user ID from the database  +++++++++++ 04-20-21
    # and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/users/<user_id>/<account_id>", methods=['GET'])
    def get_user_account(user_id, account_id):
        try:
            user = UserService.get_user(int(user_id))
            account = AccountService.get_account_id(account_id)
            # return jsonify(str(user), str(account)), 200
            return jsonify(user.json(), account.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # return jsonify(user.json(), account_id.json()), 201

    # ---------------- Update a user  with an ID and return 200 status for a successful Update  or 404 ----------------------
    @app.route("/users/<user_id>", methods=['PUT'])
    def put_user(user_id):
        try:
            user = User.json_parse(request.json)
            user.user_id = int(user_id)
            UserService.update_user(user)
            return jsonify(user.json()),
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # ----------------------------- delete with id
    @app.route("/users/<user_id>", methods=['DELETE'])
    def del_user(user_id):
        try:
            UserService.delete_user(int(user_id))
            return '', 204
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/users/<user_id>", methods=["PATCH"])
    def patch_user(user_id):
        action = request.json['action']

        # ---------------- Create new user and return 201 status code for successful creation ----------------------

    @app.route("/users", methods=['POST'])
    def post_user():
        user = User.json_parse(request.json)
        user = UserService.create_user(user)
        #return jsonify(user.json()), 201
        return jsonify(str(user)), 201

    # ---------------- Create new user account  for the same user with  ID and return 201 status code for successful creation ----------------------
    @app.route("/users/<user_id>", methods=['POST'])
    def create_user_withid(user_id):

        try:
            user_acct = UserService.get_user(int(user_id)).__dict__
            first_index = (list(user_acct.values())[0])
            print(first_index)
            # print("--------------testing-------------------")
            print(f" The value passed in is : {first_index}")
            for users in AccountService.all_account():
                # print(users)
                print()
                if list(users.values())[0] == first_index:
                    acc = Account()
                    acc.userid = first_index
                    # print(acc)
                    account = AccountService.create_account(acc)
                    # print(users)
                    return jsonify(account.json()), 201
                else:
                    print("Nothing found")

        except ResourceNotFound as r:
            return r.message, 404
# 000000000000000000000000000000000000000000000000000000000000000000000000000
#     @app.route("/users/<user_id>", methods=['GET'])
#     def get_user(user_id):
#         try:
#             user = UserService.get_user(int(user_id))
#             return jsonify(user.json()), 200
#         except ValueError as e:
#             return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
#         except ResourceNotFound as r:
#             return r.message, 404
# ----------------------------------

# @app.route("/accounts", methods=['POST'])
# def post_account():
#     account = Account.json_parse(request.json)
#     UserService.create_account(account)
#     return jsonify(account.json()), 201
#
# @app.route("/accounts", methods=['GET'])
# def all_account():
#     return jsonify(UserService.all_user()), 200
