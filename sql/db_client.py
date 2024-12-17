import psycopg2

def create_server_connection():
    PGHOST='ep-billowing-dawn-a95row8d.gwc.azure.neon.tech'
    PGDATABASE='DATAFUNDAMENTALS'
    PGUSER='DATAFUNDAMENTALS_owner'
    PGPASSWORD='IPKFE15iJuOH'

    conn = None
    try:
        conn = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=5432)
        print("Database conn successful")
    except Error as err:
        print(f"Error: '{err}'")
    return conn
connection = create_server_connection()
# ejecuto querys
# cierre cursor
# cierro conexión
connection.close()
# Crear tabla
conn = create_server_connection()
# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datafund_students table
try:
    cur.execute("""CREATE TABLE datafund_students(
                student_id SERIAL PRIMARY KEY,
                student_name VARCHAR (50) UNIQUE NOT NULL,
                student_email VARCHAR (100) NOT NULL,
                student_age INT NOT NULL);
                """)
    # Make the changes to the database persistent
    conn.commit()
except Error as err:
        print(f"Error: '{err}'")
        conn.rollback()

# Close cursor and communication with the database
cur.close()
# mas ordenes...isno cierro conexión
conn.close()


