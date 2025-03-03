import os
import mysql.connector as mysql
from python_jupiter_notes.Lesson_16 import creds
import dotenv


dotenv.load_dotenv()


db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=creds.host,
    port=creds.port,
    database=creds.database,
)
cursor = db.cursor(dictionary=True, buffered=True)


cursor.execute("SELECT * FROM students WHERE name = 'Yurii'")
print(cursor.fetchall())


db.commit()
db.close()
