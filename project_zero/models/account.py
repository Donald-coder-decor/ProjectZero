class Account:
    def __init__(self, account_id=0, account_type="", amt_dep=0, amt_withdraw=0, status=True, userid=0):
        self.account_id = account_id
        self.account_type = account_type
        self.amt_dep = amt_dep
        self.amt_withdraw = amt_withdraw
        self.status = status
        self.userid = userid

    def json(self):
        return {
            'accountId': self.account_id,
            'account_type': self.account_type,
            'amt_dep': self.amt_dep,
            'amt_withdraw': self.amt_withdraw,
            'status': self.status,
            'userId': self.userid,
        }

    @staticmethod
    def json_parse(json):
        account = Account()
        account.account_id = json["accountId"]
        account.account_type = json["account_type"]
        account.amt_dep = json["amt_dep"]
        account.amt_withdraw = json["amt_withdraw"]
        account.status = json["status"]
        account.userid = json["userId"]
        return account

    def __repr__(self):
        return str(self.json())


#
def _test():
    account = Account()
    account.deposit(100)
    account.withdraw(400)
    print(account)


# return account


if __name__ == '__main__':
    _test()
