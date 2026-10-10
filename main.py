"""Simple terminal task manager"""
def main():
    tasks = []
    while True:
        print("\n1. List 2. Add 3. Complete 4. Delete 5. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            if not tasks:
                print("No tasks.")
            else:
                for i, t in enumerate(tasks, 1):
                    status = "✓" if t["done"] else "✗"
                    print(f"{i}. [{status}] {t['desc']}")
        elif choice == "2":
            desc = input("Task: ").strip()
            if desc:
                tasks.append({"desc": desc, "done": False})
                print("Added.")
        elif choice == "3":
            idx = input("Task # to complete: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(tasks):
                    tasks[i]["done"] = True
                    print("Marked complete.")
                else:
                    print("Invalid number.")
            else:
                print("Invalid input.")
        elif choice == "4":
            idx = input("Task # to delete: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(tasks):
                    tasks.pop(i)
                    print("Deleted.")
                else:
                    print("Invalid number.")
            else:
                print("Invalid input.")
        elif choice == "5":
            print("Bye.")
            break
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main()