import flet as ft

def main(page: ft.Page):
    page.title = "App de Saludos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    saludo_contador = 0

    # Mensaje inicial
    bienvenida = ft.Text("👋 ¡Bienvenido a la App de Saludos!", size=20, weight=ft.FontWeight.BOLD)

    # Campo de entrada
    t = ft.TextField(label="Ingrese su nombre", autofocus=True, width=300)

    # Mensaje de salida
    salida = ft.Text(size=18)

    # Etiqueta de contador
    contador = ft.Text("Saludos hechos: 0", size=14, italic=True)

    # Función para saludar
    def click(e):
        nonlocal saludo_contador
        name = t.value.strip()
        if name == "":
            salida.value = "⚠️ Campo vacío. Por favor escriba su nombre."
        else:
            saludo_contador += 1
            salida.value = f"Hola {name} 👋"
            contador.value = f"Saludos hechos: {saludo_contador}"
        page.update()

    # Función para limpiar
    def limpiar(e):
        nonlocal saludo_contador
        t.value = ""
        salida.value = ""
        saludo_contador = 0
        contador.value = "Saludos hechos: 0"
        page.update()

    # Botones
    b_saludar = ft.ElevatedButton("Saludar", on_click=click)
    b_limpiar = ft.OutlinedButton("Limpiar", on_click=limpiar)

    # Agregar a la página
    page.add(
        bienvenida,
        t,
        ft.Row([b_saludar, b_limpiar], spacing=10),
        salida,
        contador,
    )

ft.app(target=main)
