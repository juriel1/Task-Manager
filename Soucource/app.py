import flet as ft
from Soucource.task import Task
from Soucource.data_manager import Data_manager

class App(ft.UserControl):
    def build(self):
        self.datamanager = Data_manager()
        self.new_task = ft.TextField(
            hint_text="Task", on_submit=self.add_task, expand=True
        )
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.filter_changed,
            tabs=[ft.Tab(text="New"), ft.Tab(text="Progress"), ft.Tab(text="Wait"), ft.Tab(text="Problems"), ft.Tab(text="Finish")],
        )

        return ft.Column(
            width=1000,
            controls=[
                ft.Row(
                    [ft.Text(value="Task Manager", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.FloatingActionButton(
                                icon=ft.icons.SAVE, on_click=lambda _:self.datamanager.save_data()),
                                ft.FloatingActionButton(
                                icon=ft.icons.CHARGING_STATION_ROUNDED, on_click=self.add_task)
                            ]
                        ),
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_task
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,                        
                    ],
                ),
            ],
        )

    async def add_task(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete,self.task_change)
            self.datamanager.set_new_task(self.new_task.value,"New")
            self.tasks.controls.append(task)
            self.new_task.value = ""
            await self.new_task.focus_async()
            await self.update_async()

    async def task_status_change(self, task:Task):
        self.datamanager.set_task(task.content.value,task.status_)
        await self.update_async()

    async def task_delete(self, task:Task):
        self.tasks.controls.remove(task)
        self.datamanager.remove_task(task.content.value)
        await self.update_async()

    async def task_change(self, otask:str,ntask:str):
        self.datamanager.change_task(otask,ntask)
        await self.update_async()

    async def filter_changed(self, e):
        await self.update_async()

    async def update_async(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                (status == "New" and task.status_ == "New")
                or (status == "Progress" and task.status_ == "Progress")
                or (status == "Wait" and task.status_ == "Wait")
                or (status == "Problems" and task.status_ == "Problems")
                or (status == "Finish" and task.status_ == "Finish")
            )
            if not task.status_:
                count += 1
        await super().update_async()