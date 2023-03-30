from datetime import datetime
from fitnessguide import db 


class Users(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_fname = db.Column(db.String(100),nullable=False)
    user_lname = db.Column(db.String(100),nullable=False)
    gender= db.Column(db.String(100),nullable=False)
    user_email = db.Column(db.String(120), unique=True) 
    user_phone=db.Column(db.String(120),nullable=True) 
    user_datereg=db.Column(db.DateTime(), default=datetime.utcnow)
    user_pwd=db.Column(db.String(120),nullable=False)

class Admin(db.Model):
    admin_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_fullname = db.Column(db.String(100),nullable=False)
    admin_email = db.Column(db.String(120)) 
    admin_password=db.Column(db.String(120),nullable=False)


class Payment(db.Model):
    pay_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    #pay_donid = db.Column(db.Integer, db.ForeignKey('donation.don_id'),nullable=True)
    pay_date = db.Column(db.DateTime(),default=datetime.utcnow)
    pay_amount = db.Column(db.Float)
    pay_status = db.Column(db.Enum('pending','failed','paid'), nullable=False, server_default=('pending'))
    pay_ref = db.Column(db.String(20),nullable=False)
    pay_userid = db.Column(db.Integer,db.ForeignKey('users.user_id'), nullable=True)


class Employment(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Environment(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Lifestyle(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Personality(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)
    
class Relationship(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    iten = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Symptoms(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Step2(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    qstn_option = db.Column(db.String(20),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Step3(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    questions = db.Column(db.String(255),nullable=False)
    qstn_option = db.Column(db.String(20),nullable=False)
    qstn_value = db.Column(db.Integer, nullable=True)

class Sed_Lifestyle(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    item = db.Column(db.String(255),nullable=False)
    No_hrs = db.Column(db.Integer,nullable=False)
    converted_value = db.Column(db.Integer, nullable=True)

class Social(db.Model):
    q_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    life_event = db.Column(db.String(255),nullable=False)
    qstn_value = db.Column(db.Integer,nullable=False)

class Options(db.Model):
    opt_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    opt_name = db.Column(db.String(50),nullable=False)


class Categories(db.Model):
    cat_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    cat_name = db.Column(db.String(1000),nullable=False)
    cat_point = db.Column(db.String(100),nullable=True)
    total_score = db.Column(db.Integer,nullable=True)

class Readjustment(db.Model):
    srs_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    srs_name = db.Column(db.String(1000),nullable=False)
    srs_score = db.Column(db.Integer,nullable=True)



