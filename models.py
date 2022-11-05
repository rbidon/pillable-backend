# import peewee to create models to use for react software
from peewee import *
import datetime
#  handling the login/logout function 
from flask_login import UserMixin

# define the database uses SqliteDatabase
DATABASE = SqliteDatabase('medication.sqlite')

class User(UserMixin):
    username =CharField(unique=True)
    # no repeat email & username
    email= CharField(unique =True)
    password = CharField()
    
    class Meta:
        database = CharField()
        
#  define my Medication Model uses class
class Medication(Model):
    name = CharField()
    quantity = CharField() #Or integerfield
    dosage_frequency = CharField()
    refill_date = DateField()
    refill_remaining = IntegerField()
    notes = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    # connect to a DATABASE & where to store its data
    class Meta:
        database = DATABASE


# define the method that will initialize the models & give it direction
def initialize():
    # connect to the database
    DATABASE.connect()  
    # create the medication DATABASE with the models 
    DATABASE.create_tables([Medication], safe=True)
    print("Connected to the DATABASE and created tables only when true")
    #  close the database when done
    DATABASE.close()