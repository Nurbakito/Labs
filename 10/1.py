import psycopg2
import csv


conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100),
        phone VARCHAR(20)
    );
""")

def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            cur.execute("""
                INSERT INTO PhoneBook (username, phone)
                VALUES (%s, %s);
            """, (row[0], row[1]))
    conn.commit()


def insert_from_console():
    username = input("Type Username: ")
    phone = input("Type phone number: ")
    cur.execute("""
        INSERT INTO PhoneBook (username, phone)
        VALUES (%s, %s);
    """, (username, phone))
    conn.commit()


def update_data(username, new_phone):
    cur.execute("""
        UPDATE PhoneBook
        SET phone = %s
        WHERE username = %s;
    """, (new_phone, username))
    conn.commit()


def query_data(filter=None):
    if filter:
        cur.execute("""
            SELECT * FROM PhoneBook
            WHERE username = %s OR phone = %s;
        """, (filter, filter))
    else:
        cur.execute("""
            SELECT * FROM PhoneBook;
        """)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(filter):
    cur.execute("""
        DELETE FROM PhoneBook
        WHERE username = %s OR phone = %s;
    """, (filter, filter))
    conn.commit()
insert_from_console()



cur.close()
conn.close()
