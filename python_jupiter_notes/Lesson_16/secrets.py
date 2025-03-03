import mysql.connector as mysql
from python_jupiter_notes.Lesson_16 import creds


db = mysql.connect(
    user=creds.user,
    passwd=creds.passwd,
    host=creds.host,
    port=creds.port,
    database=creds.database,
)
cursor = db.cursor(dictionary=True, buffered=True)


cursor.execute("SELECT * FROM students WHERE name = 'Yurii'")
print(cursor.fetchall())


db.commit()
db.close()
