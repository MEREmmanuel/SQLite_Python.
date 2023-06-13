import sqlite3


def conectar():
    conexion = sqlite3.connect('articulos.db')
    cursor = conexion.cursor()
    # print("Conectado")
    return conexion, cursor


def cerrar_conexion(conexion):
    conexion.close()


def crear_tabla():
    conexion, cursor = conectar()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS articulos (ID INT PRIMARY KEY, NOMBRE VARCHAR(20), CANTIDAD INT, IMPORTE FLOAT TEXT)')
    cerrar_conexion(conexion)
    # print("Tabla creada")


def carga_inicial():
    conexion, cursor = conectar()
    articulos = [
        (1235, "cuaderno", 25, 2.36),
        (1254, "boligrafo", 100, 0.90),
        (1345, "goma", 75, 0.50)
    ]
    cursor.executemany('INSERT INTO articulos VALUES (?,?,?,?)', articulos)
    conexion.commit()
    cerrar_conexion(conexion)
    # print("Carga inicial hecha")


def insertar_articulo(articulo):
    conexion, cursor = conectar()
    cursor.execute('INSERT INTO articulos VALUES (?,?,?,?)', articulo)
    conexion.commit()
    cerrar_conexion(conexion)
    print("Articulo insertado")


def consultar():
    conexion, cursor = conectar()
    cursor.execute('SELECT * FROM articulos')
    articulos = cursor.fetchall()
    cerrar_conexion(conexion)
    return articulos

def actualizar_articulo(id, nombre, cantidad, importe):
    conexion, cursor = conectar()
    cursor.execute(f"UPDATE articulos SET nombre='{nombre}', cantidad={cantidad}, importe={importe} WHERE id={id}")
    print("Articulo actualizado")
    conexion.commit()
    cerrar_conexion(conexion)

def borrar_articulo(id):
    conexion, cursor = conectar()
    cursor.execute(f'DELETE FROM articulos WHERE id={id}')
    conexion.commit()
    cerrar_conexion(conexion)
    print("Articulo borrado")

if __name__ == '__main__':
    crear_tabla()
    #carga_inicial()
    #articulo=(1352,"lapiz", 150, 0.60)
    #insertar_articulo(articulo)
    #actualizar_articulo(1352, "Lapiz verde", 149, 0.55)
    borrar_articulo(1352)
    articulos = consultar()
    for articulo in articulos:
        print (articulo[1])
