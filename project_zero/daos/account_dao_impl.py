from decimal import Decimal

from exceptions.resource_not_found import ResourceNotFound
from models.account import Account
from daos.account_dao import AccountDAO
# from services.account_service import AccountService
from util.db_connection import connection


class AccountDAOImpl(AccountDAO):

    def delete_account(self, account_id):
        sql = "DELETE FROM account WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()

# ------------------------------------------------------
    def update_account(self, change):
        sql = "UPDATE account SET accounttype = %s, amtdep=%s, amtwitddraw=%s , status=%s  WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, (change.accounttype, change.amtdep, change.amtwitddraw, change.status))
        connection.commit()

    def get_account_id(self, account_id):
        sql = "SELECT * FROM account WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        record = cursor.fetchone()

        if record:

            return Account(record[0], record[1], float(record[2]), float(record[3]), record[4], record[5])

        else:
            raise ResourceNotFound(f"Account with id: {account_id} - Not Found")

    def create_account(self, account):
        sql = "INSERT INTO account VALUES(DEFAULT, %s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (account.account_type, account.amt_dep, account.amt_withdraw, account.status, account.userid))
        connection.commit()
        record = cursor.fetchone()

        return Account(Account(record[0], record[1], record[2], float(record[3]), record[4]))

    def all_account(self):
        sql = "SELECT * FROM account"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account = Account(record[0], record[1], float(record[2]), float(record[3]), record[4])
            account_list.append(account.json())

        return account_list

    # def create_account1(self, account, userid):
    #     sql = "INSERT INTO account VALUES(DEFAULT, %s, %s, %s, %s, %s) RETURNING *"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, account.account_type, account.amt_dep, account.amt_withdraw, account.status, account.userid)
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     return Account(Account(record[0], record[1], float(record[2]), float(record[3]), record[4]))
