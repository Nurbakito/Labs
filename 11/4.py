import psycopg2

def create_delete_data():
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    procedure_definition = """
    CREATE OR REPLACE PROCEDURE delete_data(IN delete_criteria TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE username = delete_criteria) THEN
        DELETE FROM PhoneBook WHERE username = delete_criteria;
    
    ELSIF EXISTS (SELECT 1 FROM PhoneBook WHERE phone = delete_criteria) THEN
        DELETE FROM PhoneBook WHERE phone = delete_criteria;
    ELSE
        
        RAISE NOTICE 'No record found for the provided criteria';
    END IF;
END;
$$;

"""

    cur.execute(procedure_definition)
    conn.commit()
    
    cur.close()
    conn.close()

create_delete_data()
