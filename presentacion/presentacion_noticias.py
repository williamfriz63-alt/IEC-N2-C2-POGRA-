def mostrar_detalles_noticia(noticia):
    print(f"\n--- {noticia.titulo} ---")
    print(f"Fecha: {noticia.fecha_publicacion}")
    print(f"Contenido:\n{noticia.contenido}")
    print("----------------------------------------")