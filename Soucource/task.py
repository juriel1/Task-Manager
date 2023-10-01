import flet as ft

class Task(ft.UserControl):
    def __init__(self, content, task_status_change, task_delete):
        super().__init__()
        self.status_ = "New"
        self.content = content
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.content = ft.Text(self.content)
        self.dropdown_task = ft.Dropdown(
            on_change=self.status_changed,
            width=150,
            hint_text="New",            
            options=[
                ft.dropdown.Option("New"),
                ft.dropdown.Option("Progress"),
                ft.dropdown.Option("Wait"),
                ft.dropdown.Option("Problems"),
                ft.dropdown.Option("Finish"),
            ]
        )
        self.edit_content = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    spacing=0,
                    controls=[self.content,self.dropdown_task]
                    ),
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_task,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_task,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_content,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_edit,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    async def edit_task(self, e):
        self.edit_content.value = self.content.value
        self.display_view.visible = False
        self.edit_view.visible = True
        await self.update_async()

    async def save_edit(self, e):
        self.content.value = self.edit_content.value
        self.display_view.visible = True
        self.edit_view.visible = False
        await self.update_async()

    async def status_changed(self, e):
        self.status_ = self.dropdown_task.value
        await self.task_status_change(self)

    async def delete_task(self, e):
        await self.task_delete(self)
