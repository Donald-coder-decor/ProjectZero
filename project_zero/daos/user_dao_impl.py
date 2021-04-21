# donaldpostgre.cevirmla02ux.us-east-2.rds.amazonaws.com
from exceptions.resource_not_found import ResourceNotFound
from models.user import User
# from models.account import Account
from util.db_connection import connection

from daos.user_dao import UserDAO


class UserDAOImpl(UserDAO):

    def all_user(self):
        sql = "SELECT * FROM users"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        user_list = []
        for record in records:
            user = User(record[0], record[1], record[2], record[3])
            user_list.append(user.json())
        return user_list

    def create_user(self, user):
        sql = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (user.firstname, user.lastname, user.phone, ))
        connection.commit()
        record = cursor.fetchone()

        return User(User(record[0], record[1], record[2], record[3]))

    def create_user_wid(self, user_id):
        pass

    def get_user(self, user_id):

        sql = "SELECT * FROM users WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        record = cursor.fetchone()

        if record:
            return User(record[0], record[1], record[2], record[3])
        else:
            raise ResourceNotFound(f"User with id: {user_id} - Not Found")

    def update_user(self, change):
        sql = "UPDATE users SET firstname = %s, lastname=%s, phone=%s WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, (change.firstname, change.lastname, change.phone, change.user_id))
        connection.commit()

    def delete_user(self, user_id):
        sql = "DELETE FROM users WHERE id =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()

    # -----------------------create new account for a user ------
    #
    # def create_account(self, account, user_id):
    #
    #     sql = "INSERT INTO account VALUES(DEFAULT, %s, %s, %s, %s,%s) RETURNING *"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, (account.account_type, account.amt_dep, account.amt_withdraw, account.status))
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     # return User(User(record[0], record[1], record[2], record[3], float(record[4]), record[5], record[6], record[7], float(record[8]), record[9], record[10]))
    #     return User(User(record[0], record[1], record[2], record[3]))
    #
    # def all_account(self):
    #     sql = "SELECT * FROM account"
    #     cursor = connection.cursor()
    #     cursor.execute(sql)
    #     records = cursor.fetchall()
    #     account_list = []
    #     for record in records:
    #
    # #         user = User(record[0], record[1], record[2], record[3], record[3])
    # #         account_list.append(user.json())
    # #     return account_list
    # #


def _test():
    pass
    user_dao = UserDAOImpl()
    users = user_dao.all_user()
    # user.get_user(1)

    print(users)
    if user_dao.get_user(11):
        print(user_dao.get_user(11))
        print("found and ID")
    else:
        print("ID not found ID")


if __name__ == '__main__':
    _test()
