from task_manager import TaskManager

def main():
    manager = TaskManager()
    print("📝 Gerenciador de Tarefas (Digite 'sair' para encerrar)")
    
    while True:
        command = input("\nComandos: [adicionar, completar, listar]: ").strip().lower()
        
        if command == "sair":
            break
        
        elif command == "adicionar":
            desc = input("Descrição da tarefa: ")
            try:
                task = manager.add_task(desc)
                print(f"✅ Tarefa #{task['id']} adicionada!")
            except ValueError as e:
                print(f"❌ Erro: {e}")
        
        elif command == "completar":
            try:
                task_id = int(input("ID da tarefa: "))
                task = manager.complete_task(task_id)
                print(f"✔️ Tarefa #{task['id']} marcada como concluída!")
            except (ValueError, TypeError) as e:
                print(f"❌ Erro: {e}")
        
        elif command == "listar":
            tasks = manager.list_tasks()
            print("\n📋 Tarefas:")
            for task in tasks:
                status = "✓" if task["completed"] else " "
                print(f"{task['id']}. [{status}] {task['description']}")
        
        else:
            print("⚠️ Comando inválido.")

if __name__ == "__main__":
    main()