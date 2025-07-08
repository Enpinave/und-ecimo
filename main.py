import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto de Grupo"
    
    # Campos de entrada
    nombre = ft.TextField(label="Tu nombre")
    edad = ft.TextField(label="Tu edad")  # ← Corregido aquí
    salida = ft.Text()
    
    # Función que se ejecuta al presionar el botón
    def saludar(e):
        salida.value = f"Hola, {nombre.value}! Tienes {edad.value} años."
        page.update()

    # Botón para activar el saludo
    boton = ft.ElevatedButton("Saludar", on_click=saludar)
    
    # Añadir elementos a la página
    page.add(nombre, edad, boton, salida)

# Ejecutar la app
ft.app(target=main)
