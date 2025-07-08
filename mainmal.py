import flet as ft

def main(page: ft.Page):
    page.title = "App"

    # Elementos iniciales
    t = ft.TextField(label="Ingrese su nombre")
    salida = ft.Text()
    
    def click(e):
        name = t.value
        if name.strip() == "":
            salida.value = "⚠️ Campo vacío"
        else:
            salida.value = f"Hola {name}"
        page.update()
    
    b = ft.ElevatedButton("Saludar", on_click=click)
    
    # Añadir todo a la página
    page.add(t, b, salida)

ft.app(target=main)
