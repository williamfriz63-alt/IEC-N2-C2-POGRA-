def solicitar_datos_periodista():
    print("\n--- Registro de Nuevo Periodista ---")
    nombre = input("Ingrese el nombre completo del periodista: ")
    email = input("Ingrese el correo electrónico: ")
    contrasena = input("Ingrese la contraseña: ")
    especialidad = input("Ingrese la especialidad (ej. Política, Tecnología): ")
    rut = input("Ingrese el RUT: ")
    
    # Aquí más adelante puedes empaquetar estos datos y pasárselos a tu capa de negocio/repositorio
    print(f"\n[Éxito] Datos recopilados para el periodista: {nombre} ({especialidad})")
    
    return {
        "nombre": nombre,
        "email": email,
        "contrasena": contrasena,
        "especialidad": especialidad,
        "rut": rut
    }