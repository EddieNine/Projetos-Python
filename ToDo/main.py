import flet as ft
import json
import os

# Definindo cores e ícones
THEMES = {
    "light": {
        "primary_color": "#4CAF50",
        "background_color": "#E0FFFF",
        "text_color": "#333333",
        "button_text_color": "#FFFFFF"
    },
    "dark": {
        "primary_color": "#333333",
        "background_color": "#1E1E1E",
        "text_color": "#E0E0E0",
        "button_text_color": "#000000"
    }
}

TASKS_FILE = "tasks.json"
editing_index = None  # Variável global para rastrear o índice da tarefa sendo editada

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON. O arquivo pode estar corrompido.")
            return []
    return []

def save_tasks(task_list):
    with open(TASKS_FILE, "w") as file:
        json.dump(task_list, file)

def main(page: ft.Page):
    global editing_index
    current_theme = "light"

    def get_theme_colors(theme):
        return THEMES[theme]

    def apply_theme(theme):
        colors = get_theme_colors(theme)
        page.bgcolor = colors["background_color"]
        task_input.bgcolor = colors["primary_color"]
        add_button.bgcolor = colors["primary_color"]
        clear_button.bgcolor = colors["primary_color"]
        add_button.color = colors["button_text_color"]
        clear_button.color = colors["button_text_color"]
        task_input.color = colors["text_color"]
        theme_toggle_button.bgcolor = colors["primary_color"]
        theme_toggle_button.color = colors["button_text_color"]
        page.update()

    def toggle_theme(e):
        nonlocal current_theme
        current_theme = "dark" if current_theme == "light" else "light"
        apply_theme(current_theme)

    def add_task(e):
        task_text = task_input.value
        if task_text:
            if editing_index is not None:
                # Atualiza a tarefa existente
                task_list[editing_index]["label"] = task_text
                editing_index = None
                add_button.text = "Adicionar"
            else:
                # Adiciona uma nova tarefa
                new_task = {"label": task_text, "completed": False}
                task_list.append(new_task)

            update_task(None)  # Atualiza a lista de tarefas na interface
            task_input.value = ""
            page.update()

    def edit_task(index):
        global editing_index
        editing_index = index
        task_input.value = task_list[index]["label"]
        add_button.text = "Salvar"

    def update_task(e):
        pending_tasks.controls.clear()
        completed_tasks.controls.clear()

        for i, task in enumerate(task_list):
            checkbox = ft.Checkbox(
                label=task["label"],
                value=task["completed"],
                on_change=toggle_task_status,
                width=300,
                height=40
            )
            if task["completed"]:
                completed_tasks.controls.append(
                    ft.Row([
                        checkbox,
                        ft.IconButton(
                            icon="edit",
                            on_click=lambda e, index=i: edit_task(index)
                        )
                    ])
                )
            else:
                pending_tasks.controls.append(
                    ft.Row([
                        checkbox,
                        ft.IconButton(
                            icon="edit",
                            on_click=lambda e, index=i: edit_task(index)
                        )
                    ])
                )

        save_tasks(task_list)
        page.update()

    def toggle_task_status(e):
        task_index = [i for i, task in enumerate(task_list) if task["label"] == e.control.label][0]
        task_list[task_index]["completed"] = e.control.value
        update_task(None)

    def clear_completed(e):
        task_list[:] = [task for task in task_list if not task["completed"]]
        update_task(None)

    task_input = ft.TextField(
        hint_text="Adicione uma nova tarefa",
        width=300,
        border=ft.InputBorder.NONE
    )

    add_button = ft.ElevatedButton(
        text="Adicionar",
        icon="add",
        on_click=add_task
    )

    clear_button = ft.ElevatedButton(
        text="Remover concluídas",
        icon="clear",
        on_click=clear_completed
    )

    theme_toggle_button = ft.ElevatedButton(
        text="Alternar Tema",
        icon="brightness_6",
        on_click=toggle_theme
    )

    pending_tasks = ft.Column()
    completed_tasks = ft.Column()

    task_list = load_tasks()
    apply_theme(current_theme)

    page.add(
        ft.Column([
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            theme_toggle_button,
            ft.Text("Para Concluir", weight=ft.FontWeight.BOLD, size=20),
            pending_tasks,
            ft.Text("Tarefas Concluídas", weight=ft.FontWeight.BOLD, size=20),
            completed_tasks,
            clear_button
        ], width=400, alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
