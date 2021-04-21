from models.user import User


# Temporal database

class TempDB:
    users = {
        1: User(user_id=1, firstname="Don",   lastname="Nteh", phone=4020001234 ),
        1: User(user_id=1, firstname="Destiny", lastname="Steban", phone=7020421234),
       #  2: User(user_id=2, firstname="Caroline", middlename="Marie", lastname="Tegouaket", phone=4022051234, email="caroline@yahoo.com",address="1111 S D street, apt 102 Lincoln NE , 68508",acount_type="Checking Account",amount_dep=50, amount_withdraw="",status=True),
        # 3: User(user_id=3, firstname="Ornella", middlename="Johnson", lastname="Sandy", phone=5020001234, email="ornella@yahoo.com",address="1023 NW Y street, apt 112 Lincoln NE , 68510",acount_type="Checking Account",amount_dep=5000, amount_withdraw="",status=True),
        # 4: User(user_id=4, firstname="Destiny", middlename="Steban", lastname="Batela", phone=7020421234, email="steban@yahoo.com",address="2005 SW P street, apt 250 Lincoln NE , 68508",acount_type="Savings Account",amount_dep=10000, amount_withdraw="",status=True),
        # 5: User(user_id=5, firstname="Tinashe", middlename="Fonyuy", lastname="Abigail", phone=3080201234, email="tinashe@yahoo.com",address="1115 N west street, apt 5 Lincoln NE , 68808",acount_type="Savings Account",amount_dep=7500, amount_withdraw="",status=True),
    }

