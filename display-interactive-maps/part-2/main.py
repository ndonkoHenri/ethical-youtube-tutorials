import flet as ft
import flet.map as map


def main(page: ft.Page):
    page.add(
        m:=map.Map(
            expand=True,
            on_init=lambda e: print("Map Init"),
            on_tap=lambda e: print("Map was Tapped"),
            layers=[
                map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                ),
            ],
        ),
        ft.Row(
            controls=[
                ft.OutlinedButton("Rotate 90°", on_click=lambda e: m.rotate_from(90)),
                ft.OutlinedButton("Rotate -90°", on_click=lambda e: m.rotate_from(-90)),
                ft.OutlinedButton("Move to (40, 50)", on_click=lambda e: m.move_to(destination=map.MapLatitudeLongitude(40, 50), animation_duration=ft.Duration(seconds=1))),
                ft.OutlinedButton("Zoom in", on_click=lambda e: m.zoom_in(animation_duration=ft.Duration(seconds=4))),
                ft.OutlinedButton("Zoom out", on_click=lambda e: m.zoom_out(animation_duration=ft.Duration(seconds=4))),
                ft.OutlinedButton("Zoom to 5", on_click=lambda e: m.zoom_to(5)),
                ft.OutlinedButton("Center on ", on_click=lambda e: m.center_on(point=map.MapLatitudeLongitude(40, 50), zoom=4)),
            ]
        )
    )


ft.app(main)
