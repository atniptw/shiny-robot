from peewee import *

db = SqliteDatabase('nfl.db')

class Team(Model):
    name = CharField()
    conference = CharField()
    division = CharField()
    
    class Meta:
        database = db
