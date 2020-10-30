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
      while True:
           print('Elige que parte del CRUD quieres hacer:')
           num = int(input('1.Crear   2.Leer    3.Actualizar    4.Borrar    5.Salir --> '))
           if num == 1:
              print('En que tabla quieres insertar datos?')
              num2 = int(input('1.Repartidores   2.Cloros    3.Piscinas    4.Relaciones    5.Volver --> '))
              if num2 == 1:
                  with conexion.cursor() as cursor:
                   id = input('Introduce el ID --> ')                
                   dni = input('Introduce el dni --> ')
                   nombre = input('Introduce el nombre --> ')
                   apellidos = input('Introduce los apellidos --> ')
                   consulta = ('INSERT INTO repartidor(id,dni,nombre,apellidos) values ('+id+',\''+dni+'\',\''+nombre+'\',\''+apellidos+'\');')
                   cursor.execute(consulta)
                   conexion.commit()
              elif num2 == 2:
                  with conexion.cursor() as cursor:
                   id = input('Introduce el ID --> ') 
                   codigo = input('Introduce el código --> ')
                   nombre = input('Introduce el nombre --> ')
                   tipo = input('Introduce el tipo --> ')
                   consulta = ('INSERT INTO cloro(id,cod,nombre,tipo) values ('+id+',\''+codigo+'\',\''+nombre+'\',\''+tipo+'\');')
                   cursor.execute(consulta)
                   conexion.commit()
              elif num2 == 3:
                  with conexion.cursor() as cursor:
                   id = input('Introduce el ID --> ') 
                   dni = input('Introduce el dni del propietario --> ')
                   nombre = input('Introduce el nombre del propietario --> ')
                   direccion = input('Introduce la dirección del propietario --> ')
                   consulta = ('INSERT INTO piscina(id,dni,nombre,direccion) values ('+id+',\''+dni+'\',\''+nombre+'\',\''+direccion+'\');')
                   cursor.execute(consulta)
                   conexion.commit()
              elif num2 == 4:
                  with conexion.cursor() as cursor:
                   id_relacion = input('Introduce el ID de la relación --> ') 
                   id_repartidor = input('Introduce el ID del repartidor --> ')
                   id_cloro = input('Introduce el ID del cloro --> ')
                   id_piscina = input('Introduce el ID de la piscina --> ')
                   consulta = ('INSERT INTO relación(id,dni,nombre,direccion) values ('+id+',\''+dni+'\',\''+nombre+'\',\''+direccion+'\');')
                   cursor.execute(consulta)
                   conexion.commit()     
              elif num2 == 5:
                  print('Cargando Menú Principal')
              else:
                  print('**Opción incorrecta**')
           elif num == 2:
                    print('De que tabla quieres leer? ')
                    num2 = int(input('1.Repartidores   2.Cloros    3.Piscinas    4.Relaciones    5.Volver --> '))
                    if num2 == 1:
                     with conexion.cursor() as cursor:
                        consulta = ("select * from repartidor")
                        cursor.execute(consulta)
                        repartidor = cursor.fetchone()
                        while repartidor:
                         print(repartidor)
                         repartidor = cursor.fetchone()
                    elif num2 == 2:
                     with conexion.cursor() as cursor:
                        consulta = ("select * from cloro")
                        cursor.execute(consulta)
                        cloro = cursor.fetchone()
                        while cloro:
                         print(cloro)
                         cloro = cursor.fetchone()
                    elif num2 == 3:
                     with conexion.cursor() as cursor:
                        consulta = ("select * from piscina")
                        cursor.execute(consulta)
                        piscina = cursor.fetchone()
                        while piscina:
                         print(piscina)
                         piscina = cursor.fetchone()
                    elif num2 == 4:
                     with conexion.cursor() as cursor:
                        consulta = ("select * from relacion")
                        cursor.execute(consulta)
                        relacion = cursor.fetchone()
                        while relacion:
                         print(relacion)
                         piscina = cursor.fetchone()
                    elif num2 == 5:
                         print('Cargando Menú Principal') 
                    else:
                         print('**Opción incorrecta**')
           elif num == 3:
                    print('Qué tabla quieres actualizar? ')
                    num2 = int(input('1.Repartidores   2.Cloros    3.Piscinas    4.Relaciones    5.Volver --> '))
                    if num2 == 1:
                        print('Qué campo quieres cambiar?')
                        num3 = int(input('1.ID   2.DNI    3.Nombre    4.Apellidos    5.Volver --> '))
                        if num3 == 1:
                         with conexion.cursor() as cursor:
                          id = input('Introduce el número de ID que quieres actualizar --> ')
                          id2 = input('Introduce el número de ID por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE REPARTIDOR SET ID='+id2+' WHERE ID='+id+';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 2:
                         with conexion.cursor() as cursor:
                          dni = input('Introduce el número de DNI que quieres actualizar --> ')
                          dni2 = input('Introduce el número de DNI por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE REPARTIDOR SET DNI=\''+dni2+'\' WHERE DNI=\''+dni+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 3:
                         with conexion.cursor() as cursor:
                          nombre = input('Introduce el nombre que quieres actualizar --> ')
                          nombre2 = input('Introduce el nombre por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE REPARTIDOR SET NOMBRE=\''+nombre2+'\' WHERE NOMBRE=\''+nombre+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 4:
                         with conexion.cursor() as cursor:
                          apellidos = input('Introduce los apellidos que quieres actualizar --> ')
                          apellidos2 = input('Introduce los apellidos por los que quieres cambiarlos --> ')
                          consulta = ('UPDATE REPARTIDOR SET APELLIDO=\''+apellidos2+'\' WHERE APELLIDOS=\''+apellidos+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 5:
                            print('Cargando Menú Principal')
                        else:
                         print('**Opción incorrecta**')
                    elif num2 == 2:
                        print('Qué campo quieres cambiar?')
                        num3 = int(input('1.ID   2.Código    3.Nombre    4.Tipo    5.Volver --> '))
                        if num3 == 1:
                         with conexion.cursor() as cursor:
                          id = input('Introduce el número de ID que quieres actualizar --> ')
                          id2 = input('Introduce el número de ID por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE CLORO SET ID='+id2+' WHERE ID='+id+';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 2:
                         with conexion.cursor() as cursor:
                          cod = input('Introduce el código que quieres actualizar --> ')
                          cod2 = input('Introduce el código por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE CLORO SET COD=\''+cod2+'\' WHERE COD=\''+cod+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 3:
                         with conexion.cursor() as cursor:
                          nombre = input('Introduce el nombre que quieres actualizar --> ')
                          nombre2 = input('Introduce el nombre por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE CLORO SET NOMBRE=\''+nombre2+'\' WHERE NOMBRE=\''+nombre+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 4:
                         with conexion.cursor() as cursor:
                          tipo = input('Introduce el tipo que quieres actualizar --> ')
                          tipo2 = input('Introduce el tipo por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE CLORO SET TIPO=\''+tipo2+'\' WHERE TIPO=\''+tipo+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 5:
                          print('Cargando Menú Principal')
                        else:
                         print('**Opción incorrecta**')
                    elif num2 == 3:
                        print('Qué campo quieres cambiar?')
                        num3 = int(input('1.ID   2.DNI del Propietario    3.Nombre    4.Dirección    5.Volver --> '))
                        if num3 == 1:
                         with conexion.cursor() as cursor:
                          id = input('Introduce el número de ID que quieres actualizar --> ')
                          id2 = input('Introduce el número de ID por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE PISCINA SET ID='+id2+' WHERE ID='+id+';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 2:
                         with conexion.cursor() as cursor:
                          dni = input('Introduce el DNI que quieres actualizar --> ')
                          dni2 = input('Introduce el DNI por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE PISCINA SET DNI=\''+dni2+'\' WHERE DNI=\''+dni+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 3:
                         with conexion.cursor() as cursor:
                          nombre = input('Introduce el nombre que quieres actualizar --> ')
                          nombre2 = input('Introduce el nombre por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE PISCINA SET NOMBRE=\''+nombre2+'\' WHERE NOMBRE=\''+nombre+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 4:
                         with conexion.cursor() as cursor:
                          direc = input('Introduce la dirección que quieres actualizar --> ')
                          direc2 = input('Introduce la dirección por la que quieres cambiarla --> ')
                          consulta = ('UPDATE PISCINA SET DIRECCION=\''+direc2+'\' WHERE DIRECCION=\''+direc+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 5:
                          print('Cargando Menú Principal')
                        else:
                         print('**Opción incorrecta**')
                    elif num2 == 4:
                        print('Qué campo quieres cambiar?')
                        num3 = int(input('1.ID   2.DNI del Propietario    3.Nombre    4.Dirección    5.Volver --> '))
                        if num3 == 1:
                         with conexion.cursor() as cursor:
                          id = input('Introduce el número de ID que quieres actualizar --> ')
                          id2 = input('Introduce el número de ID por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE PISCINA SET ID='+id2+' WHERE ID='+id+';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 2:
                         with conexion.cursor() as cursor:
                          dni = input('Introduce el DNI que quieres actualizar --> ')
                          dni2 = input('Introduce el DNI por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE PISCINA SET DNI=\''+dni2+'\' WHERE DNI=\''+dni+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 3:
                         with conexion.cursor() as cursor:
                          nombre = input('Introduce el nombre que quieres actualizar --> ')
                          nombre2 = input('Introduce el nombre por el que quieres cambiarlo --> ')
                          consulta = ('UPDATE PISCINA SET NOMBRE=\''+nombre2+'\' WHERE NOMBRE=\''+nombre+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 4:
                         with conexion.cursor() as cursor:
                          direc = input('Introduce la dirección que quieres actualizar --> ')
                          direc2 = input('Introduce la dirección por la que quieres cambiarla --> ')
                          consulta = ('UPDATE PISCINA SET DIRECCION=\''+direc2+'\' WHERE DIRECCION=\''+direc+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                        elif num3 == 5:
                          print('Cargando Menú Principal')
                        else:
                         print('**Opción incorrecta**')     
                    elif num2 == 5:
                        print('Cargando Menú Principal')
                    else:
                         print('**Opción incorrecta**')
           elif num == 4:
                    print('De qué tabla quieres borrar datos? ')
                    num2 = int(input('1.Repartidores   2.Cloros    3.Piscinas    4.Relaciones    5.Volver --> '))
                    if num2 == 1:
                        with conexion.cursor() as cursor:
                         id = input("Introduce el ID del Repartidor que quieres eliminar -->")
                         consulta = ('DELETE FROM REPARTIDOR WHERE id =\''+id+'\';')
                         cursor.execute(consulta)
                         conexion.commit()
                    elif num2 == 2:
                         with conexion.cursor() as cursor:
                          id = input("Introduce el ID del Cloro que quieres eliminar -->")
                          consulta = ('DELETE FROM CLORO WHERE id =\''+id+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                    elif num2 == 3:
                         with conexion.cursor() as cursor:
                          id = input("Introduce el ID la Piscina que quieres eliminar -->")
                          consulta = ('DELETE FROM PISCINA WHERE id =\''+id+'\';')
                          cursor.execute(consulta)
                          conexion.commit()
                    elif num2 == 4:
                         with conexion.cursor() as cursor:
                          id = input("Introduce el ID la Piscina que quieres eliminar -->")
                          consulta = ('DELETE FROM PISCINA WHERE id =\''+id+'\';')
                          cursor.execute(consulta)
                          conexion.commit()      
                    elif num2 == 5:
                        print('Cargando Menú Principal')
                    else:
                         print('**Opción incorrecta**')
           elif num == 5:
                     print('Adiós!!')
                     break
           else:
                     print('**Opción incorrecta**')

    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
