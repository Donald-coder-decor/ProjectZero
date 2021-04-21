from flask import jsonify, request
from models.user import User
from exceptions.resource_not_found import ResourceNotFound
from models.account import Account
from services.account_service import AccountService
from services.user_service import UserService


def route(app):
    @app.route("/accounts", methods=['GET'])
    def get_all_account():
        return jsonify(AccountService.all_account()), 200

    # ---------------- Retrieve user with a specific ID from the database and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/accounts/<account_id>", methods=['GET'])
    def get_account_id(account_id):
        try:
            account = AccountService.get_account_id(int(account_id))
            return jsonify(account.json()), 200
        except ValueError as e:
            return "Not a valid ID     or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # ---------------- Create new user and return 201 status code for successful creation ----------------------

    @app.route("/accounts", methods=['POST'])
    def post_account():

        account = Account.json_parse(request.json)
        account = AccountService.create_account(account)
        return jsonify(account.json()), 201

    # ________________ fetch all accounts that have a client____________
    @app.route("/users/<userid>/accounts", methods=['GET'])
    def get_all_acct(userid):
        try:
            if UserService.get_user(userid):
                return jsonify(AccountService.all_account()), 200
        except ResourceNotFound as r:
            r.message
            return "This client does not exist", 404

    # ------------------------------------------------------------------------
    @app.route("/users/<userid>/accounts/<accounts_id>", methods=['GET'])
    def get_accounts(userid, accounts_id):
        try:
            if UserService.get_user(userid):
                acct = AccountService.get_account_id(int(accounts_id))
                return jsonify(acct.json()), 200
        except ValueError as e:
            return f"{userid} is not a valid ID", 400
        except ResourceNotFound as rf:
            rf.message
            return "Account does not exist", 404

    # -----------------------update an account with and ID
    @app.route("/users/<userid>/accounts/<accounts_id>", methods=['UPDATE'])
    def update_accounts(userid, accounts_id):
        try:
            if UserService.get_user(userid):
                acct = AccountService.update_account(int(accounts_id))
                return jsonify(acct.json()), 200
        except ValueError as e:
            return f"{userid} is not a valid ID", 400
        except ResourceNotFound as rf:
            rf.message
            return "Account does not exist", 404

        # -----------------------Delete an account with and ID

    @app.route("/users/<userid>/accounts/<accounts_id>", methods=['DELETE'])
    def delete_accounts(userid, accounts_id):
        try:
            if UserService.get_user(userid):
                AccountService.get_account_id(accounts_id)
                AccountService.delete_account(accounts_id)
                return '', 204

        except ResourceNotFound as rf:
            rf.message
            return "Account does not exist", 404

    # # ------------ PATCH, UPDATE DEPOSITE AMOUNT------

    @app.route("/users/<user_id>/accounts/<account_id>", methods=['PATCH'])
    def patch_accounts(user_id, account_id):
        choose_action = request.json['deposit_amount']

        if choose_action == 'deposit_amount' or choose_action == 'withdraw_amount':
            try:
                balance = AccountService.deposit(int(account_id), user_id) if choose_action == 'deposit_amount' else AccountService.withdraw_amount( int(account_id), user_id)
                return f"{balance} is a success!", 200
            except ResourceNotFound as ve:
                return "Not enough funds", 422
            except ResourceNotFound as ve:
                return "This Client does not exist", 404
        return choose_action
