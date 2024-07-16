import flet as ft
import flet.map as map


def main(page: ft.Page):
    page.window.always_on_top = True

    def handle_tap(e: map.MapTapEvent):
        print(e)

    page.add(
        map.Map(
            expand=True,
            configuration=map.MapConfiguration(
                on_init=lambda e: print("Map Init"),
                on_tap=handle_tap,
                on_long_press=handle_tap,
            ),
            layers=[
                map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    on_image_error=lambda e: print("Image Error"),
                ),
                map.CircleLayer(
                    circles=[
                        map.CircleMarker(
                            radius=20,
                            coordinates=map.MapLatitudeLongitude(54, 41),
                            color=ft.colors.BLUE,
                            border_color=ft.colors.random_color(),
                            border_stroke_width=5,
                        )
                    ]
                ),
                map.PolygonLayer(
                    polygons=[
                        map.PolygonMarker(
                            label="Random Label",
                            label_text_style=ft.TextStyle(
                                color=ft.colors.GREEN, size=19
                            ),
                            color=ft.colors.random_color(),
                            coordinates=[
                                map.MapLatitudeLongitude(11, -11),
                                map.MapLatitudeLongitude(23, -10),
                                map.MapLatitudeLongitude(6, 1),
                            ],
                        )
                    ]
                ),
                map.PolylineLayer(
                    polylines=[
                        map.PolylineMarker(
                            color=ft.colors.random_color(),
                            border_stroke_width=10,
                            coordinates=[
                                map.MapLatitudeLongitude(10, 10),
                                map.MapLatitudeLongitude(30, 13),
                                map.MapLatitudeLongitude(23, 40),
                            ],
                        )
                    ]
                ),
                map.MarkerLayer(
                    markers=[
                        map.Marker(
                            content=ft.Icon(
                                ft.icons.random_icon(),
                                color=ft.colors.random_color(),
                                size=30,
                            ),
                            coordinates=map.MapLatitudeLongitude(35, 35),
                        )
                    ]
                ),
                map.RichAttribution(
                    alignment=ft.alignment.top_center,
                    attributions=[
                        map.TextSourceAttribution(
                            text="Flet",
                            prepend_copyright=False,
                            on_click=lambda e: page.launch_url("https://flet.dev"),
                        )
                    ],
                ),
                map.SimpleAttribution(
                    text="Simple Attr.", alignment=ft.alignment.top_center
                ),
            ],
        )
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)
