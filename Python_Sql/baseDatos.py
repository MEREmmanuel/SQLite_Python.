import sqlite3


def conectar():
    con = sqlite3.connect('pruebas.db')  # ':memory'
    cursor = con.cursor()
    return con, cursor

# Creamos la tabla


def crearTabla(conexion, cursor):
    sentencia = """
    CREATE TABLE IF NOT EXISTS usuarios
    (ID INTEGER PRIMARY KEY NOT NULL,
    USUARIO TEXT NOT NULL, 
    EMAIL TEXT NOT NULL,
    CLAVE TEXT NOT NULL);
    """
    cursor.execute(sentencia)
    conexion.close()
    print('Tabla creada correctamente')

# Insertamos datos a la tabla


def insertarDatos(conexion, cursor, datos):
   # sentencia = """
   # INSERT INTO usuarios
   # (ID, USUARIO, EMAIL, CLAVE) VALUES (1, 'MEREmmanuel', 'rsb02_99@hotmail.com', 'Djrosemm87#')
   # """
    sentencia = "INSERT INTO usuarios VALUES (NULL, ?, ?, ?)"
   # cursor.execute(sentencia, datos)
    cursor.executemany(sentencia, datos)
   # cursor.execute(sentencia)
    print('Datos ingresador correctamente')
    conexion.commit()
    conexion.close()

# Consultados todos los datos de la tabla


def consultarDatos01(conexion, cursor):
    sentencia = """SELECT * FROM usuarios
    """
    resultado = cursor.execute(sentencia)
    # print(cursor.fetchall())
    for fila in resultado:
        print(fila)
    conexion.close()

# Consultamso las 2 primeras filas, id, usuario y email


def consultarDatos(conexion, cursor):
    sentencia = "SELECT id,usuario,email FROM usuarios "  # LIMIT 2
    resultado = cursor.execute(sentencia)
    # conexion.close()
    return resultado

# Traemos los datos email, clave según el nombre


def consultarDatosId(conexion, cursor, nombre):
    sentencia = f"SELECT email, clave FROM usuarios WHERE usuario = '{nombre}'"
    resultado = cursor.execute(sentencia)
    return resultado

# Actualizamos el nombre del usuario segun su id


def actualizarDatos(conexion, cursor, id, nombre):
    sentencia = f"""UPDATE usuarios set usuario='{nombre}' WHERE id={id}"""
    cursor.execute(sentencia)
    conexion.commit()
    print("Datos actualizados correctamente")
    return True

# Eliminamos la tabla segun el id de usuario


def eliminarDatos(conexion, cursor, id):
    sentencia = f"""DELETE from usuarios WHERE id={id}"""
    cursor.execute(sentencia)
    conexion.commit()
    print('Datos eliminados correctamente')
    return True


# Nuestro main
if __name__ == '__main__':
    con, cursor = conectar()
    # print(con)
    # print(cursor)
    # crearTabla(con, cursor)
    # insertarDatos(con, cursor)
    datos = [('MARTINEZ', 'informatica_21887038@cintalapa.tecnm', 'Djrosemm99'),
             ('ROSEMBERG', "hola@homtail.com", "djrosemm7")]
    # insertarDatos(con,cursor,datos)
    resultado = consultarDatos(con, cursor)
    for fila in resultado:
        print("*"*100)
        print("\n")
        print("ID: ", fila[0])
        print("NOMBRE: ", fila[1])
        print("EMAIL", fila[2])
        print("\n")

    resultado = consultarDatosId(con, cursor, 'MEREmmanuel')
    print(resultado)
    for fila in resultado:
        print(fila)

    actualizarDatos(con, cursor, 1, 'REMEmmanuel')

    eliminarDatos(con,cursor,1)