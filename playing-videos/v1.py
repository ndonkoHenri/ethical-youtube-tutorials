import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.always_on_top = True

    page.add(
        ft.Video(
            playlist=[
                # ft.VideoMedia(resource="/Users/ndonkohenri/PycharmProjects/Ethical-FletTutorials/playing-video/assets/vid-1.flv"),
                ft.VideoMedia(
                    resource="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/VolkswagenGTIReview.mp4"
                ),
                ft.VideoMedia(
                    resource="https://videos.pexels.com/video-files/3196600/3196600-uhd_2560_1440_25fps.mp4"
                ),
            ],
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.colors.LIGHT_BLUE,
            aspect_ratio=16 / 9,
            volume=100,
            autoplay=False,
            muted=False,
            show_controls=True,
            expand=True,
            on_error=lambda e: print(f"Video Error: {e.data}"),
            on_loaded=lambda e: print("Video loaded!"),
            on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
            on_exit_fullscreen=lambda e: print("Video exited fullscreen!"),
        ),
    )


ft.app(main, assets_dir="assets")
