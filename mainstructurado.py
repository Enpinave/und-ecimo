import flet as ft

def mostrar_mensaje(salida, nombre):
    if not nombre.strip():
        salida.value = "⚠️ Por favor, escribe tu nombre."
        salida.color = ft.colors.RED
    else:
        salida.value = f"🎉 ¡Hola, {nombre}!"
        salida.color = ft.colors.INDIGO
        

def main(page: ft.Page):
    page.title = "✨ Aplicación Organizada"
    page.bgcolor = ft.colors.LIGHT_GREEN_100
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campo de texto estilizado
    nombre_input = ft.TextField(
        label="🧑 Tu nombre",
        width=300,
        filled=True,
        fill_color=ft.colors.WHITE,
        border_color=ft.colors.GREEN_400,
        border_radius=8
    )

    # Texto de salida
    salida = ft.Text(size=20, weight="bold")

    # Botón estilizado
    boton_saludo = ft.ElevatedButton(
        text="Saludar 🌟",
        on_click=lambda e: [mostrar_mensaje(salida, nombre_input.value), page.update()],
        bgcolor=ft.colors.GREEN_400,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), elevation=5)
    )

    # Contenedor tipo tarjeta
    tarjeta = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("🙌 Bienvenido a la App de Saludo", size=25, weight="bold", color=ft.colors.GREEN_800),
                nombre_input,
                boton_saludo,
                salida
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=30,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.GREY_500, spread_radius=2),
    )

    page.add(tarjeta)

ft.app(target=main)
