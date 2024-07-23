import flet as ft


def main(page: ft.Page):
    def handle_change(e: ft.ControlEvent):
        if e.control.value is True:
            # Enable the browser context menu if the switch is on
            e.page.browser_context_menu.enable()
        else:
            # Disable the browser context menu if the switch is off
            e.page.browser_context_menu.disable()

    page.add(
        ft.Switch(
            label="Enable Browser Context Menu",
            value=True,
            on_change=handle_change
        )
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)
