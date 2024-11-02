import flet as ft

# Gist containing test videos: https://gist.github.com/jsturgis/3b19447b304616f18657
# IPTV repo: https://github.com/iptv-org/iptv


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.always_on_top = True

    def handle_new_source(e: ft.ControlEvent):
        # page.can_launch_url(str)
        video.playlist_add(ft.VideoMedia(resource=e.control.value)) # creates a VideoMedia and add it to the playlist
        video.jump_to(len(video.playlist) - 1)  # jump to the last media of the playlist (which is the one we added)

    page.add(
        ft.TextField(
            label="Video Source",
            value="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
            on_submit=handle_new_source,    # will be called when the user submits the content of the field (ex: by pressing Enter)
        ),
        video := ft.Video(
            playlist=[
                ft.VideoMedia(resource="https://user-images.githubusercontent.com/28951144/229373718-86ce5e1d-d195-45d5-baa6-ef94041d0b90.mp4")
            ],
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.BLUE,
            aspect_ratio=16 / 9,
            volume=100,
            autoplay=False,
            muted=False,
            expand=True,
        ),
    )


ft.app(main, assets_dir="assets")
