import flet as ft

def main(page: ft.Page):
    page.title = "App"
    def click(e):
        name = t.value
        if name == "":
            page.controls.append(ft.Text("Campo vacío"))
        else:
            page.controls.append(ft.Text("Hola " + name))
        page.update()
    t = ft.TextField()
    b = ft.ElevatedButton("Saludar", on_click=click)
    page.controls.append(t)
    page.controls.append(b)
    page.update()

ft.app(target=main)
