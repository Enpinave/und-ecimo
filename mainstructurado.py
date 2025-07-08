import flet as ft

def mostrar_mensaje(salida, nombre):
    if not nombre.strip():
        salida.value = "Por favor, escribe tu nombre."
        salida.color = "red"
    else:
        salida.value = f"Hola, {nombre}!"
        salida.color = "purple"

def main(page: ft.Page):
    page.title = "Aplicación organizada"
    
    nombre_input = ft.TextField(label="Tu nombre", width=300)
    salida = ft.Text()

    boton_saludo = ft.ElevatedButton(
        text="Saludar",
        on_click=lambda e: [mostrar_mensaje(salida, nombre_input.value), page.update()]
    )

    page.add(nombre_input, boton_saludo, salida)

ft.app(target=main)
