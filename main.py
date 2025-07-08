import flet as ft

def main(page: ft.Page):
    page.title = "🎓 Proyecto de Grupo"
    page.bgcolor = ft.colors.CYAN_100  # Fondo general más colorido
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campos de entrada con color de fondo
    nombre = ft.TextField(
        label="📛 Tu nombre",
        width=300,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        border_color=ft.colors.BLUE_300
    )

    edad = ft.TextField(
        label="🎂 Tu edad",
        width=300,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        border_color=ft.colors.PINK_300
    )

    salida = ft.Text(size=20)

    def saludar(e):
        if nombre.value.strip() == "" or edad.value.strip() == "":
            salida.value = "⚠️ Por favor, completa todos los campos."
            salida.color = ft.colors.RED
        else:
            salida.value = f"👋 ¡Hola, {nombre.value}! 🎉 Tienes {edad.value} años."
            salida.color = ft.colors.PURPLE
        page.update()

    boton = ft.ElevatedButton(
        text="✨ Saludar 😊",
        on_click=saludar,
        bgcolor=ft.colors.DEEP_PURPLE_300,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            elevation=5
        )
    )

    # Contenedor blanco con borde redondeado
    tarjeta = ft.Container(
        content=ft.Column(
            [
                ft.Text("🎈 Bienvenido a la app del grupo 🎈", size=25, weight="bold", color=ft.colors.BLUE_900),
                nombre,
                edad,
                boton,
                salida
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=30,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.GREY_500, spread_radius=2)
    )

    page.add(tarjeta)

ft.app(target=main)
