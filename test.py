import sqlite3

fname = input("Ism: ")
lname = input("Familiya: ")
age = int(input("Yosh: "))

values = (fname, lname, age)

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()

    # Agar jadval bo‘lsa, o‘chirib tashlaymiz
    cursor.execute("DROP TABLE IF EXISTS test")

    # Yangi jadval yaratamiz
    cursor.execute("""
                   CREATE TABLE test
                   (
                       fname TEXT,
                       lname TEXT,
                       age   INT
                   )
                   """)

    # Ma’lumot qo‘shamiz
    cursor.execute("INSERT INTO test VALUES (?, ?, ?)", values)

    conn.commit()

print("✅ Ma’lumot bazaga qo‘shildi!")

