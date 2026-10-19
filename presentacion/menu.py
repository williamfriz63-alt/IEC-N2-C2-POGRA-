import sys
from datos import nombre_app, version_app, main_menu
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
            print('\n--- Redirigiendo a Gestión de Usuarios y Perfiles ---')
            # Aquí llamarás a las funciones de usuarios o menú de periodistas/lectores
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