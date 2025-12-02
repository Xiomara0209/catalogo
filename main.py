import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="tienda_virtual"
    )

def registrar_usuario():
    print("\n--- REGISTRAR USUARIO ---")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    provincia = input("Provincia: ")
    pais = input("Pais: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
        INSERT INTO usuarios (nombre, apellido, email, password, telefono, direccion)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    datos = (nombre, apellido, email, password, telefono, direccion)

    cursor.execute(query, datos)
    conexion.commit()

    print("\nUsuario registrado con éxito.\n")

    cursor.close()
    conexion.close()


# INICIAR SESIÓN
# -------------------------------------
def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    email = input("Email: ")
    password = input("Contraseña: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT id, nombre, apellido FROM usuario_tienda WHERE email = %s AND contraseña = %s"
    cursor.execute(query, (email, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        print(f"\nBienvenido {resultado[1]} {resultado[2]} (ID: {resultado[0]})\n") #type: ignore
    else:
        print("\nCredenciales incorrectas.\n")

    cursor.close()
    conexion.close()

def consultar_usuario():
    print("\n--- CONSULTAR USUARIO ---")
    user_id = input("ID del usuario: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuario_tienda WHERE id = %s", (user_id,))
    resultado = cursor.fetchone()

    if resultado:
        print("\nDatos del usuario:")
        print(resultado)
    else:
        print("\nNo existe un usuario con ese ID.")

    cursor.close()
    conexion.close()

def modificar_usuario():
    print("\n--- MODIFICAR DATOS ---")
    user_id = input("ID del usuario: ")

    nuevo_telefono = input("Nuevo teléfono: ")
    nueva_direccion = input("Nueva dirección: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
        UPDATE usuario_tienda
        SET telefono = %s, direccion = %s
        WHERE id = %s
    """

    cursor.execute(query, (nuevo_telefono, nueva_direccion, user_id))
    conexion.commit()

    print("\nDatos modificados correctamente.\n")

    cursor.close()
    conexion.close()

def modificar_password():
    print("\n--- CAMBIAR CONTRASEÑA ---")
    user_id = input("ID del usuario: ")
    nueva_pass = input("Nueva contraseña: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = "UPDATE usuarios SET password = %s WHERE id = %s"
    cursor.execute(query, (nueva_pass, user_id))
    conexion.commit()

    print("\nContraseña actualizada.\n")

    cursor.close()
    conexion.close()

def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    user_id = input("ID del usuario: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    conexion.commit()

    print("\nUsuario eliminado correctamente.\n")

    cursor.close()
    conexion.close()


def menu():
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Consultar usuario")
        print("4. Modificar datos")
        print("5. Cambiar contraseña")
        print("6. Eliminar usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            consultar_usuario()
        elif opcion == "4":
            modificar_usuario()
        elif opcion == "5":
            modificar_password()
        elif opcion == "6":
            eliminar_usuario()
        elif opcion == "7":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()