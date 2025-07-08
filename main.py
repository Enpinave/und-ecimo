import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto de Grupo"
    
    nombre = ft.TextField(label="Tu nombre")
    edad = ft.TextField(label="Tu edad")
    salida = ft.Text()
    
    def saludar(e):
        salida.value = f"Hola, {nombre.value}! Tienes {edad.value} años."
        page.update()

    boton = ft.ElevatedButton("Saludar", on_click=saludar)
    
    page.add(nombre, edad, boton, salida)

ft.app(target=main)
