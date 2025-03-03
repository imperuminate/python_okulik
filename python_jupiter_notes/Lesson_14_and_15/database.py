import mysql.connector as mysql


# Создание подключения и курсора
db = mysql.connect(
    user="st4",
    passwd="AVNS_ANI6HFK07yLk4d9l4Nq",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st4",
)
cursor = db.cursor(dictionary=True, buffered=True)


cursor.execute("SELECT * FROM students WHERE name = 'Yurii'")
data = cursor.fetchall()
# Поиск по имени, и вывод только фамилий из найденного в поиске
for data_dict in data:
    print(data_dict["second_name"])


# Поиск во всей таблице, но вывод только одной последней записи
cursor.execute("SELECT * FROM students ORDER BY id DESC")
data2 = cursor.fetchone()
print(data2)


# Нормальный запрос с подстановкой данных
user_name = "Yurii"
user_second_name = "Andreiko"
cursor.execute(f"SELECT * FROM students WHERE name = '{user_name}' and second_name = '{user_second_name}'")
print(cursor.fetchone())


# Запрос с иньекцией (Yurii'; -- )
query_injection = "SELECT * FROM students WHERE name = '{0}' and second_name = '{1}'"
cursor.execute(query_injection.format(input("name:"), input("second name:")))
print(cursor.fetchall())


# Правильный запрос с защитой от иньекцией в правильном формате %s. Либа сама обезопасит
query_injection = "SELECT * FROM students WHERE name = %s and second_name = %s "
cursor.execute(query_injection, (input("name"), input("name2")))
print(cursor.fetchall())


cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Гамаз и его великие идеи', 400)")
book_id = cursor.lastrowid
print(book_id)
query = "SELECT * FROM books WHERE id = %s"
cursor.execute(query, (book_id,))
print(cursor.fetchone())


# Как отправить сразу несколько запросов с разными данными в подстановке
books_data = [("Гамаз и его мелкие шалости", 400), ("Гамаз просто танцует. Том 1", 400)]
query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(query, books_data)


# Запрос с длинной строкой
cursor.execute("""SELECT * 
               FROM students 
               WHERE name = 'Yurii'""")
data = cursor.fetchall()
print(data)


# Нужно комитнуть изменения в базе, чтобы они применились. А потом и закрыть базу
db.commit()
db.close()
