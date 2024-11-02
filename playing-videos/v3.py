import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.always_on_top = True

    page.add(
        ft.Video(
            playlist=[
                ft.VideoMedia(resource="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4"),
            ],
            fill_color=ft.colors.BLACK,
            expand=True,
            autoplay=True,
            volume=60,
            subtitle_configuration=ft.VideoSubtitleConfiguration(
                src="subtitles-1.srt", # path or link to a subtitle file
                title="A title",
                language="en",
                text_style=ft.TextStyle(
                    size=45,
                    color=ft.colors.RED,
                    weight=ft.FontWeight.BOLD,
                    bgcolor=ft.colors.WHITE,
                )
            )

        ),
    )


ft.app(main, assets_dir="assets")
