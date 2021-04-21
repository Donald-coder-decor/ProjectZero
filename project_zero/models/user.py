class User:

    def __init__(self, user_id=0, firstname="", lastname="", phone=0, ):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone

    def json(self):
        return {
            'userid': self.user_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'phone': self.phone,

        }

    @staticmethod
    def json_parse(json):
        user = User()
        user.user_id = json["userid"]
        user.firstname = json["firstname"]
        user.lastname = json["lastname"]
        user.phone = json["phone"]

        return user

    def __repr__(self):
        return str(self.json())
