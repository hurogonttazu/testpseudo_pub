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
# SELECT
conn = create_server_connection()

cur = conn.cursor()

cur.execute('SELECT * FROM datafund_students;')
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()
for row in rows:
    print(row)