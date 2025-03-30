class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str) -> dict:
        """Adiciona uma nova tarefa."""
        if not description.strip():
            raise ValueError("Descrição não pode ser vazia.")
        task = {"id": len(self.tasks) + 1, "description": description, "completed": False}
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: int) -> dict:
        """Marca tarefa como concluída."""
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            raise ValueError("Tarefa não encontrada.")
        task["completed"] = True
        return task

    def list_tasks(self) -> list:
        """Retorna todas as tarefas."""
        return self.tasks.copy()