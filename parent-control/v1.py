import flet as ft


def main(page: ft.Page):
    x = ft.Text("Hello, world!", size=42)

    y = ft.Container(
        height=300,
        width=300,
        bgcolor=ft.Colors.BLUE,
        content=x,
    )

    page.add(y)

    print(type(x.parent))
    print(type(y.parent))


ft.app(main)
