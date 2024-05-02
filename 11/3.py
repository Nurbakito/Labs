import psycopg2

def create_insert_data():
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    procedure_definition = """
    CREATE OR REPLACE PROCEDURE insert_data(IN new_username VARCHAR(100), IN new_phone VARCHAR(20))
LANGUAGE plpgsql
AS $$
BEGIN
    
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE username = new_username) THEN
        
        UPDATE PhoneBook SET phone = new_phone WHERE username = new_username;
    ELSE
    
        INSERT INTO PhoneBook (username, phone) VALUES (new_username, new_phone);
    END IF;
END;
$$;

"""

    cur.execute(procedure_definition)
    conn.commit()
    
    cur.close()
    conn.close()

create_insert_data()
