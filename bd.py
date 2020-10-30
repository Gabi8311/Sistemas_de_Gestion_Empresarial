import psycopg2

try:
    credenciales = {
        "dbname": "Ejercicio1",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432
    }
    conexion = psycopg2.connect(**credenciales)
    try:
        with conexion.cursor() as cursor:
            consulta = ("select dni,nombre,apellidos from repartidor")
            cursor.execute(consulta)
            repartidor = cursor.fetchone()
            while repartidor:
                print(repartidor)
                repartidor = cursor.fetchone()

    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)

except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
finally:
    conexion.close()
