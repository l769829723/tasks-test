import uuid
import datetime
import peewee

from main.settings import DB_URL
from passlib.context import CryptContext


__all__ = ['User', 'MODEL_TABLES', 'DATABASE']

DATABASE = peewee.SqliteDatabase(DB_URL)

PWDCTX = CryptContext(
  schemes=["sha256_crypt", "des_crypt"]
)

def encrypt_password(password):
  return PWDCTX.hash(password)

def verify_password(string, password):
  return PWDCTX.verify(string, password)

class BaseModel(peewee.Model):
  class Meta:
    database = DATABASE
  
  def to_dict(self):
    return self.__dict__.get('_data')


class User(BaseModel):
  ROLES = [
    ('ADMIN', 'admin'),
    ('USER', 'user')
  ]
  username = peewee.CharField(max_length=255, help_text='user login name')
  secret = peewee.CharField(max_length=77, help_text='user login password')
  role = peewee.CharField(max_length=5, choices=ROLES, help_text='user login type')
  locked = peewee.BooleanField(default=True, help_text='user is locked')

  def __init__(self, *args, **kwargs):
    self._secret_schemes = [
      "sha256_crypt", 
      "des_crypt"
    ]
    self._secret_ctx = CryptContext(
      schemes=self._secret_schemes
    )
    super(User, self).__init__(*args, **kwargs)
  
  def __str__(self):
    return self.username

  def to_dict(self):
    data = super(User, self).to_dict()
    data.pop('secret')
    data.setdefault('user_id', self.id)
    return data

  @property
  def password(self):
    return self.secret

  @password.setter
  def password(self, password):
    self.secret = self._secret_ctx.hash(password)

  def verify(self, password):
    return self._secret_ctx.verify(password, self.secret)


class Article(BaseModel):
   user = peewee.ForeignKeyField(User)
   content = peewee.TextField(help_text='Content of your write.')
   author = peewee.CharField(max_length=255, help_text='Author of this content.')
   write_at = peewee.DateTimeField(default=datetime.datetime.now(), help_text='When the write time.')
   votes = peewee.IntegerField(help_text='How many people to vote.')
   comments = peewee.IntegerField(help_text='How many people to comment.')
   published = peewee.BooleanField(default=False, help_text='Is publish now?')

   def __str__(self):
     return self.content

MODEL_TABLES = [User, Article]
