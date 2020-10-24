import sqlite3
import datetime


#hacer la conexión
conexion = sqlite3.connect('notebook.db')

#Primero hay que crear un cursor
cursor = conexion.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(255),
    apellido varchar(255),
    direccion varchar(255),
    barrio varchar(255),
    telefono int(40),
    condicion varchar(255),
    venta_alquiler varchar(255),
    mts2cubiertos int,
    mts2descubiertos int,
    mts2valorestrenar float,
    mts2valorventa float,
    valortotal float,
    hijos varchar(255),
    mascotas varchar(255),
    profesion varchar(255),
    fecha_profesion date,
    observaciones text
);
""")

#para guardar cambios 
conexion.commit()

class Ingresos:
    def abrir(self):
        conexion=sqlite3.connect('notebook.db')
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="""INSERT INTO clientes(nombre, apellido, direccion, barrio, telefono, condicion, venta_alquiler, mts2cubiertos, mts2descubiertos, mts2valorestrenar, mts2valorventa, valortotal, hijos, mascotas, profesion, fecha_profesion, observaciones) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

      
    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="SELECT * FROM clientes WHERE nombre=? and apellido=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def todo(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT * FROM clientes ORDER BY ID ASC"
        cursor.execute(sql)
        return cursor.fetchall()
       
    def baja(self,datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="DELETE FROM clientes WHERE nombre=? and apellido=?"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
        return cursor.rowcount
        