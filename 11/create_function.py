import psycopg2
from config import load_config


def create_function(sql_query):
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
            CREATE OR REPLACE FUNCTION get_parts_by_vendor(id INTEGER)
            RETURNS TABLE(part_id INTEGER, part_name VARCHAR) AS
            $$
            BEGIN
            RETURN QUERY

            SELECT parts.part_id, parts.part_name
            FROM parts
            INNER JOIN vendor_parts on vendor_parts.part_id = parts.part_id
            WHERE vendor_id = id;

            END; $$

            LANGUAGE plpgsql;
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

    create_function(query2)