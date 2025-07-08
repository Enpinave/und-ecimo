import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "🎈 Saludos App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.CYAN_100  # Fondo claro y colorido

    # Campo de entrada con estilo
    t = ft.TextField(
        label="📝 Escribe tu nombre",
        width=300,
        border_color=ft.colors.TEAL,
        filled=True,
        fill_color=ft.colors.TEAL_50,
    )

    # Texto de salida
    salida = ft.Text(size=20, weight=ft.FontWeight.BOLD)

    # Botón con color y emoji
    b = ft.ElevatedButton(
        text="Saludar 👋",
        on_click=lambda e: saludar(e),
        color=ft.colors.WHITE,
        bgcolor=ft.colors.TEAL_400
    )

    def saludar(e):
        name = t.value.strip()
        if name == "":
            salida.value = "⚠️ ¡Campo vacío!"
            salida.color = ft.colors.RED
        else:
            salida.value = f"🎉 ¡Hola, {name}!"
            salida.color = ft.colors.TEAL
        page.update()

    # Tarjeta contenedora
    card = ft.Container(
        content=ft.Column(
            controls=[t, b, salida],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=350,
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.BLACK26, spread_radius=2),
    )

    page.add(card)

ft.app(target=main)
