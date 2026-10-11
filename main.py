"""Terminal Task Manager: add, list, done, delete tasks."""

tasks = []
next_id = 1

def add(desc):
    global next_id
    tasks.append({'id': next_id, 'desc': desc, 'done': False})
    print(f"Added task {next_id}")
    next_id += 1

def list_tasks():
    for t in tasks:
        status = '✓' if t['done'] else '✗'
        print(f"{t['id']}: [{status}] {t['desc']}")

def done(id_):
    for t in tasks:
        if t['id'] == id_:
            t['done'] = True
            print(f"Task {id_} marked done")
            return
    print(f"Task {id_} not found")

def delete(id_):
    global tasks
    before = len(tasks)
    tasks = [t for t in tasks if t['id'] != id_]
    print(f"Deleted {before - len(tasks)} task(s)")

def main():
    while True:
        try: