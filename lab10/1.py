import psycopg2
import csv

conn = psycopg2.connect(host="localhost", dbname="Phonebook", user="postgres",
                        password="261815121103", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL
)
""")

check = True
command = ''
temp = ''

name_var = ''
surname_var = ''
phone_var = ''
id_var = ''

start = True
back = False

back_com = ''
name_upd = ''
surname_upd = ''
phone_upd = ''

filepath = ''

while check:
    if start == True or back == True:
        start = False
        print("""
        List of the commands:
        1. Type "i" or "I" in order to INSERT data to the table.
        2. Type "u" or "U" in order to UPDATE data in the table.
        3. Type "q" or "Q" in order to make specidific QUERY in the table.
        4. Type "d" or "D" in order to DELETE data from the table.
        5. Type "f" or "F" in order to close the program.
        6. Type "s" or "S" in order to see the values in the table.
        """)
        command = str(input())

        if command == "i" or command == "I":
            print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
            command = ''
            temp = str(input())
            if temp == "con":
                name_var = str(input("Name: "))
                surname_var = str(input("Surname: "))
                phone_var = str(input("Phone: "))
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name_var, surname_var, phone_var))
                conn.commit()
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True
            if temp == "csv":
                filepath = "/mnt/data/student.csv"# Указываем файл student.csv
                try:
                    print(f"Attempting to read file: {filepath}")
                    with open(filepath, 'r') as f:
                        reader = csv.reader(f)
                        next(reader)  # Пропустить заголовок
                        for row in reader:
                            print(f"Inserting row: {row}")  # Отладочный вывод
                            cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
                    conn.commit()
                    print("Data from student.csv has been successfully inserted into the phonebook.")
                except FileNotFoundError:
                    print(f"File {filepath} not found. Please make sure it exists in the same directory as the script.")
                except Exception as e:
                    print(f"An error occurred: {e}")

                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

        if command == "d" or command == "D":
            back = False
            command = ''
            phone_var = str(input('Type phone number which you want to delete: '))
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_var,))
            conn.commit()
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True

        if command == 'u' or command == 'U':
            back = False
            command = ''
            temp = str(input('Type the name of the column that you want to change: '))
            if temp == "name":
                name_var = str(input("Enter name that you want to change: "))
                name_upd = str(input("Enter the new name: "))
                cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (name_upd, name_var))
                conn.commit()
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "surname":
                surname_var = str(input("Enter surname that you want to change: "))
                surname_upd = str(input("Enter the new surname: "))
                cur.execute("UPDATE phonebook SET surname = %s WHERE surname = %s", (surname_upd, surname_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "phone":
                phone_var = str(input("Enter phone number that you want to change: "))
                phone_upd = str(input("Enter the new phone number: "))
                cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (phone_upd, phone_var))
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

        if command == "q" or command == "Q":
            back = False
            command = ''
            temp = str(input("Type the name of the column which will be used for searching data: "))
            if temp == "id":
                id_var = str(input("Type id of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (id_var, ))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "name":
                name_var = str(input("Type name of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE name = %s", (name_var, ))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "surname":
                surname_var = str(input("Type surname of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE surname = %s", (surname_var, ))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

            if temp == "phone":
                phone_var = str(input("Type phone number of the user: "))
                cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone_var, ))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                back_com = str(input('Type "back" in order to return to the list of the commands: '))
                if back_com == "back":
                    back = True

        if command == "s" or command == "S":
            back = False
            command = ''
            cur.execute("SELECT * from phonebook;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            back_com = str(input('Type "back" in order to return to the list of the commands: '))
            if back_com == "back":
                back = True

        if command == "f" or command == "F":
            command = ''
            check = False

conn.commit()
cur.close()
conn.close()
