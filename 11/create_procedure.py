import psycopg2
from config import load_config


def create_procedure(sql_query):
    """ Create a function in the specified table """
    # sql query to create said function

    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                
                # create a function for the specified table
                cur.execute(sql_query)
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    query1 = """
            CREATE OR REPLACE PROCEDURE add_new_part(
                new_part_name varchar,
                new_vendor_name varchar
            ) 
            AS $$
            DECLARE
                v_part_id INT;
                v_vendor_id INT;
            BEGIN
                -- insert into the parts table
                INSERT INTO parts(part_name) 
                VALUES(new_part_name) 
                RETURNING part_id INTO v_part_id;
                
                -- insert a new vendor
                INSERT INTO vendors(vendor_name)
                VALUES(new_vendor_name)
                RETURNING vendor_id INTO v_vendor_id;
                
                -- insert into vendor_parts
                INSERT INTO vendor_parts(part_id, vendor_id)
                VALUEs(v_part_id, v_vendor_id);
                
            END; $$
            
            LANGUAGE PLPGSQL;           
            """
    
    query2 = """
            CREATE OR REPLACE FUNCTION get_all_vendors()
            RETURNS TABLE(vendor_id INTEGER, vendor_name VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT * FROM vendors;

            END; $$

            LANGUAGE plpgsql;
            """

    create_procedure(query1)