import os


# database setting
DB_TYPE='sqlite'
DB_NAME='db.sqlite'


BASE_DIR = os.path.dirname(__file__)
DB_URL = os.path.join(BASE_DIR, DB_NAME)
