# details: https://medium.com/p/98e2c60dfab8

import flet as ft


# before
def main1(page: ft.Page):
    def handle_tile_removal(e: ft.ControlEvent):
        icon_button = e.control
        tile = icon_button.data
        lv.controls.remove(tile)
        page.update()

    lv = ft.ListView()

    for i in range(6):
        t = ft.ListTile(title=ft.Text(f"Click the delete icon to delete Tile {i}"))
        t.trailing = ft.IconButton(
            ft.icons.DELETE_FOREVER,
            on_click=handle_tile_removal,
            data=t,
        )
        lv.controls.append(t)

    page.add(lv)


# after
def main2(page: ft.Page):
    def handle_tile_removal(e: ft.ControlEvent):
        icon_button = e.control
        tile = icon_button.parent
        lv = tile.parent
        lv.controls.remove(tile)
        page.update()

    page.add(
        ft.ListView(
            controls=[
                ft.ListTile(
                    title=ft.Text(f"Click the delete icon to delete Tile {i}"),
                    trailing=ft.IconButton(
                        ft.Icons.DELETE_FOREVER,
                        on_click=handle_tile_removal,
                    ),
                )
                for i in range(6)
            ]
        )
    )


# ft.app(main1)
ft.app(main2)
