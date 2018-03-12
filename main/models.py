from peewee import *
from main.settings import DB_URL

database = SqliteDatabase(DB_URL)

class BaseModel(Model):

  def to_dict(self):
    pass
  
  class Meta:
    database = database


class User(BaseModel):
  id = UUIDField(index=True, unique=True, primary_key=True)
  username = CharField(unique=True, max_length=255, help_text='Authenticate user name.')
  password_text = CharField(
