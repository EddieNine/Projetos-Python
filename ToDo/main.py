import flet as ft
import json
import os

# Definindo cores
PRIMARY_COLOR = "#4CAF50"
BACKGROUND_COLOR = "#E0FFFF"
TEXT_COLOR = "#333333"
BUTTON_TEXT_COLOR = "#FFFFFF"
TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.bgcolor = BACKGROUND_COLOR
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = "adaptive"

    tasks = load_tasks()

    def add_task(e):
        task_text = task_input.value
        if task_text:
            new_task = {"label": task_text, "completed": False}
            tasks.append(new_task)
            pending_tasks.controls.append(ft.Checkbox(label=task_text, value=False, on_change=update_task))
            save_tasks(tasks)
            task_input.value = ""
            page.update()

    def update_task(e):
        pending_tasks.controls.clear()
        completed_tasks.controls.clear()

        for i, task in enumerate(tasks):
            checkbox = ft.Checkbox(label=task["label"], value=task["completed"], on_change=toggle_task_status)
            if task["completed"]:
                completed_tasks.controls.append(checkbox)
            else:
                pending_tasks.controls.append(checkbox)

        save_tasks(tasks)
        page.update()

    def toggle_task_status(e):
        task_index = [i for i, task in enumerate(tasks) if task["label"] == e.control.label][0]
        tasks[task_index]["completed"] = e.control.value
        update_task(None)

    def clear_completed(e):
        tasks[:] = [task for task in tasks if not task["completed"]]
        update_task(None)

    task_input = ft.TextField(
        hint_text="Adicione uma nova tarefa",
        width=300,
        bgcolor=PRIMARY_COLOR,
        color=BUTTON_TEXT_COLOR,
        border=ft.InputBorder.NONE,
    )

    add_button = ft.ElevatedButton(
        text="Adicionar",
        on_click=add_task,
        bgcolor=PRIMARY_COLOR,
        color=BUTTON_TEXT_COLOR,
    )

    clear_button = ft.ElevatedButton(
        text="Remover concluídas",
        on_click=clear_completed,
        bgcolor=PRIMARY_COLOR,
        color=BUTTON_TEXT_COLOR,
    )

    pending_tasks = ft.Column()
    completed_tasks = ft.Column()

    update_task(None)

    page.add(
        ft.Column([
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Text("Para Concluir", weight=ft.FontWeight.BOLD, size=20, color=PRIMARY_COLOR),
            pending_tasks,
            ft.Text("Tarefas Concluídas", weight=ft.FontWeight.BOLD, size=20, color=PRIMARY_COLOR),
            completed_tasks,
            clear_button
        ], width=400, alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
