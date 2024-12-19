import psycopg2


def create_server_connection(PGHOST, PGDATABASE, PGUSER, PGPASSWORD):
    PGHOST= 'ep-billowing-dawn-a95row8d.gwc.azure.neon.tech'
    PGDATABASE= 'DATAFUNDAMENTALS'
    PGUSER='DATAFUNDAMENTALS_owner'
    PGPASSWORD= 'IPKFE15iJuOH' 
    conn = None
    try:
        conn = psycopg2.connect(database=PGDATABASE, user=PGUSER,
                                password=PGPASSWORD, host=PGHOST, port=5432)
        print("Database conn successful")
    except Exception as err:
        print(f"Error: '{err}'")

    return conn