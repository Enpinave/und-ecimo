import flet as ft

def mostrar_mensaje(page, nombre):
    if not nombre.strip():
        mensaje = ft.Text("Por favor, escribe tu nombre.", color="red")
    else:
        mensaje = ft.Text(f"Hola, {nombre}!", color="green")
    page.controls.append(mensaje)
    page.update()

def main(page: ft.Page):
    page.title = "Aplicación organizada"

    nombre_input = ft.TextField(label="Tu nombre", width=300)
    boton_saludo = ft.ElevatedButton(
        text="Saludar",
        on_click=lambda e: mostrar_mensaje(page, nombre_input.value)
    )

    page.add(nombre_input, boton_saludo)

ft.app(target=main)
