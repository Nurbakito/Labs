import psycopg2

def create_by_username():
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    function_definition = """
    CREATE OR REPLACE FUNCTION byusername(username_pattern VARCHAR(100))
RETURNS TABLE (
    id INTEGER,
    username VARCHAR(100),
    phone VARCHAR(20)
) AS $$
BEGIN
    RETURN QUERY 
        SELECT PhoneBook.id, PhoneBook.username, PhoneBook.phone 
        FROM PhoneBook 
        WHERE PhoneBook.username = username_pattern;
END;
$$ LANGUAGE plpgsql;
"""

    cur.execute(function_definition)
    conn.commit()
    
    cur.close()
    conn.close()

create_by_username()
