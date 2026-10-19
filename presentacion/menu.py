import sys
from datos import nombre_app, version_app, main_menu
from presentacion.menu_periodista import solicitar_datos_periodista
# Aquí puedes importar tus futuros módulos de presentación específicos
# from presentacion.presentacion_noticias import ...

def menu_principal():
    print(f'{nombre_app} {version_app}')
    print('=' * len(nombre_app) + "=" + '=' * len(version_app))

    while True:
        for clave, valor in main_menu.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input('Ingrese una opción [1-4]: ')

        if opcion_usuario == '1':
            print('\n--- Redirigiendo a Gestión de Periodistas ---')
            datos_nuevo_periodista = solicitar_datos_periodista()  # 👈 Guardamos el diccionario que retorna
            
            print("\n¡Periodista registrado con éxito en la interfaz!")
            # Opcional: puedes imprimir algo de los datos para verificar
            print(f"Datos recibidos: {datos_nuevo_periodista}")
            
            input("\nPresiona ENTER para volver al menú principal...")  # 👈 Esto frena la pantalla para que leas   
    
        elif opcion_usuario == '2':
            print('\n--- Redirigiendo a Gestión de Noticias y Categorías ---')
            # Aquí llamarás a las funciones de noticias
        elif opcion_usuario == '3':
            print('\n--- Redirigiendo a Gestión de Comentarios ---')
            # Aquí llamarás a las funciones de comentarios
        elif opcion_usuario == '4':
            print('Saliendo de Sistema')
            sys.exit()
        else:
            print('Opción Ingresada NO corresponde...\nIngrese nuevamente.\n')