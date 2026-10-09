"""Simple terminal task manager."""
def main():
    tasks = []
    while True:
        print("\n1. List tasks\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            if not tasks:
                print("No tasks.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == "2":
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                print("Task added.")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                idx = int(input("Task number to remove: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx-1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()