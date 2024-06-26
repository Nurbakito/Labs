import psycopg2

def create_get_phonebook():
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    function_definition = """
    CREATE OR REPLACE FUNCTION get_phonebook()
RETURNS TABLE (
    id INTEGER,
    username VARCHAR(100),
    phone VARCHAR(20)
) AS $$
BEGIN
    RETURN QUERY SELECT * FROM PhoneBook;
END;
$$ LANGUAGE plpgsql;
"""

    cur.execute(function_definition)
    conn.commit()
    
    cur.close()
    conn.close()

create_get_phonebook()