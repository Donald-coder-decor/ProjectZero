from flask import request, jsonify

from daos.account_dao_impl import AccountDAOImpl
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models import account
from models.account import Account


class AccountService:
    account_serv = AccountDAOImpl()

    @classmethod
    def create_account(cls, account):
        return cls.account_serv.create_account(account)

    @classmethod
    def all_account(cls):
        return cls.account_serv.all_account()

    @classmethod
    def get_account_id(cls, account_id):
        return cls.account_serv.get_account_id(account_id)

    # ---- update account with an ID
    @classmethod
    def update_account(cls, account_id):
        return cls.account_serv.update_account(account_id)

    # ----------------Delete account by id

    @classmethod
    def delete_account(cls, account_id):
        return cls.account_serv.delete_account(account_id)
#  user can deposit money
    @classmethod
    def deposit_amount(cls, account_id, client_id):
        try:
            acct = cls.account_dao.get_account(account_id, client_id)
            amount: float
            acct.account_balance += amount
            cls.update_account(acct, client_id)
            return acct.account_balance
        except ResourceUnavailable as e:
            return "Opps,tThe client or account does not exists", 404
        except ResourceNotFound as r:
            return "There is not enough money"
# -- user can withdraw money
    @classmethod
    def withdraw_amount(cls, account_id, client_id):
        try:
            acct = cls.account_dao.get_account(account_id, client_id)
            amount: float
            acct.account_balance -= amount
            cls.update_account(acct, client_id)
            return acct.account_balance
        except ResourceUnavailable as e:
            return "The client or account exists", 404
        except ResourceNotFound as r:
            return "There is not enough found", 422


