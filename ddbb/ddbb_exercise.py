import sqlite3

conexion = sqlite3.connect('ejemplo.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar dni, nombres, edades y emails
cursor.execute(
    "CREATE TABLE users_complete (dni VARCHAR(9) PRIMARY KEY, nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO users_complete VALUES ('09787265C', 'Hector', 27, 'hector@ejemplo.com')")

# Guardamos los cambios haciendo un commit
conexion.commit()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM users_complete")

# Mostrar el cursos a ver que hay ?
print(cursor)

# Recorremos el primer registro con el método fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)

# Creamos una lista con varios usuarios
usuarios = [('09783637P', 'Mario', 51, 'mario@ejemplo.com'),
            ('09723433J', 'Mercedes', 38, 'mercedes@ejemplo.com'),
            ('02343244H', 'Juan', 19, 'juan@ejemplo.com'),
            ]

# Ahora utilizamos el método executemany() para insertar varios
cursor.executemany("INSERT INTO users_complete VALUES (?, ?, ?, ?)", usuarios)

# Guardamos los cambios haciendo un commit
conexion.commit()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM users_complete")

# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)

conexion.close()
