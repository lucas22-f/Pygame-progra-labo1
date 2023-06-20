import sqlite3
ruta = "database/space-attack.db"
with sqlite3.connect(ruta) as conexion:
    try:
        query = """ create table jugadores 
                    (
                        id integer primary key autoincrement,
                        nombre text,
                        puntaje integer,
                        tiempo integer
                    ) 
                """
        conexion.execute(query)
        print("se creo la tabla jugadores")
    except sqlite3.OperationalError:
        print("Base de datos conectada")


def insertar_dato_en_tabla(jugador):    
    with sqlite3.connect(ruta) as conexion:
        try:
            #creamos la sentencia y ejecutamos por nombre
            respuesta = conexion.execute("SELECT puntaje FROM jugadores where nombre = ?",(jugador['nombre'],))
            resultado = respuesta.fetchone()
            #pregunto si el select que hice viene vacio o si el puntaje actual es mayor que el resultado que esta guardado en la bd
            if resultado is None or jugador['puntaje'] > resultado[0]:

                #si esta vacio significa que no existe en la bd , entonces lo creo
                if resultado is None:
                    conexion.execute("INSERT INTO jugadores(nombre, puntaje, tiempo) VALUES (?, ?, ?)", (jugador['nombre'], jugador['puntaje'], jugador['tiempo']))
                else:
                    #si no , lo actualizamos ya que el resultado que esta guardado con el nombre del jugador anterior ya existe
                    # solo cambiamos el valor del puntaje por el mas alto.
                    conexion.execute("UPDATE jugadores SET puntaje = ?, tiempo = ? WHERE nombre = ?", (jugador['puntaje'], jugador['tiempo'], jugador['nombre']))
                conexion.commit()  
        except:
            print("Error al insertar en la tabla")
         
         
def traer_tabla_ordenada():
    with sqlite3.connect(ruta) as conexion:
        try:
            respuesta = conexion.execute("SELECT * from jugadores ORDER BY puntaje DESC LIMIT 15")
            lista_jugadores = respuesta.fetchall()
            return lista_jugadores
        except:
            print("Error al traer lista de jugadores")
       
