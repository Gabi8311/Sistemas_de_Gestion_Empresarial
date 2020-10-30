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
            num = 0
            print('Elige que BBDD deseas ver:')
        while True:
            num = int(input('1.Repartidores   2.Cloros    3.Piscinas    4.Salir'))
            if num == 1:
               with conexion.cursor() as cursor:
                 consulta = ("select * from repartidor")
                 cursor.execute(consulta)
                 repartidor = cursor.fetchone()
                 while repartidor:
                  print(repartidor)
                  repartidor = cursor.fetchone()
               
                  
            elif num == 2:
                with conexion.cursor() as cursor:
                 consulta = ("select * from cloro")
                 cursor.execute(consulta)
                 cloro = cursor.fetchone()
                 while cloro:
                  print(cloro)
                  cloro = cursor.fetchone()
               
            elif num == 3:
                with conexion.cursor() as cursor:
                 consulta = ("select * from piscina")
                 cursor.execute(consulta)
                 piscina = cursor.fetchone()
                 while piscina:
                  print(piscina)
                  piscina = cursor.fetchone()
               
            elif num == 4:
                print('Adiós')
                conexion.close()
                break
            else:
                print('Número erróneo')
    except psycopg2.Error as e:
     print("Ocurrió un error al conectar a PostgreSQL: ", e)
except psycopg2.Error as e:
 print("Ocurrió un error al conectar a PostgreSQL: ", e)

