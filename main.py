import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto de Grupo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    nombre = ft.TextField(label="Tu nombre", width=300)
    edad = ft.TextField(label="Tu edad", width=300)
    salida = ft.Text(size=18, weight=ft.FontWeight.BOLD)

    def saludar(e):
        salida.value = f"Hola, {nombre.value}! Tienes {edad.value} años."
        page.update()

    boton = ft.ElevatedButton(
        "Saludar",
        on_click=saludar,
        bgcolor=ft.colors.LIGHT_BLUE_300,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    tarjeta = ft.Container(
        content=ft.Column(
            [
                nombre,
                edad,
                boton,
                salida
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        bgcolor=ft.colors.LIGHT_BLUE_50,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.BLUE_100, offset=ft.Offset(2, 2))
    )

    page.add(tarjeta)

ft.app(target=main)
