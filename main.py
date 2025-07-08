import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto de Grupo"
    nombre = ft.TextField(label="Tu nombre")
    salida = ft.Text()
    
    def saludar(e):
        salida.value = f"Hola, {nombre.value}!"
        page.update()

    boton = ft.ElevatedButton("Saludar", on_click=saludar)
    
    page.add(nombre, boton, salida)

ft.app(target=main)
