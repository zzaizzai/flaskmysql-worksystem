import os
from dotenv import load_dotenv
import mysql.connector


load_dotenv(verbose=True)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = os.environ.get("DB_USER")
HOST = os.environ.get("HOST")
TABLE = os.environ.get("TABLE")
USER_PW = os.environ.get("USER_PW")


db = mysql.connector.connect(
    host=HOST,
    user=DB_USER,
    passwd=USER_PW,
    db=TABLE,
)


cur = db.cursor(dictionary=True)

