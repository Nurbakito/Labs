import psycopg2

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT * FROM PhoneBook")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
