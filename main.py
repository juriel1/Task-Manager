import flet as ft
from Soucource.app import App

async def main(page: ft.Page):
    page.title = "Task M"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window_max_height = 2880
    page.window_max_width = 1200
    page.window_min_height = 400
    page.window_min_width = 500

    await page.add_async(App())

ft.app(main)