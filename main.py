We need to write a small terminal task manager. Under 60 lines, single file, short module docstring, standard library only, include a __main__ block. We need to limit to 60 lines. Provide code only. Let's design simple task manager that can add tasks, list tasks, mark them done, delete tasks, maybe all in memory. Use argparse for command line interface. We'll have subcommands: add, list, done, delete. Use a simple file-based persistence? But maybe keep in memory only. But for a task manager, persistence is nice. But requirement didn't say persistence; but to be useful, we might store tasks in a JSON file. Use standard library json, os.

We need to implement simple commands. Keep tasks as list of dict with "id", "desc", "done". Use simple incremental id.

File path: tasks.json in current directory.

Implement functions: load_tasks, save_tasks, add_task, list_tasks, done_task, delete_task.

Add a small module docstring. Under 60 lines. Let's count.

We'll have:

1: """Simple terminal task manager."""
2: import os, json, argparse, sys
3: 
4: TASK_FILE = 'tasks.json'
5: ...
Let's design.

We must fit within 60 lines. Let's try.

We'll write code like:

import os, json, argparse, sys

TASK_FILE = 'tasks.json'

def load():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE) as f:
        return json.load(f)

def save(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def next_id(tasks):
    return max((t['id'] for t in tasks), default=0)+1

def add(desc):
    tasks=load()
    tasks.append({'id':next_id(tasks),'desc':desc,'done':False})
    save(tasks)
    print('Added task.')

def list():
    tasks=load()
    for t in tasks:
        status='✓' if t['done'] else '✗'
        print(f"{t['id']}. [{status}] {t['desc']}")

def done(id):
    tasks=load()
    for t in tasks:
        if t['id']==id:
            t['done']=True
            save(tasks)
            print('Marked done.')
            return
    print('Task not found.')

def delete(id):
    tasks=load()
    new=[t for t in tasks if t['id']!=id]
    if len(new)==len(tasks):
        print('Task not found.')
        return
    save(new)
    print('Deleted.')

def main():
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest='cmd')
    sub.add_parser('add', help='Add a task').add_argument('desc')
    sub.add_parser('list', help='List tasks')
    sub.add_parser('done', help='Mark task done').add_argument('id', type=int)
    sub.add_parser('del', help='Delete task').add_argument('id', type=int)
    args=parser.parse_args()
    if args.cmd=='add': add(args.desc)
    elif args.cmd=='list': list()
    elif args.cmd=='done': done(args.id)
    elif args.cmd=='del': delete(args.id)
    else: parser.print_help()

if __name__=='__main__':
    main()

Line count: Let's count lines:

1: """Simple terminal task manager."""
2: import os, json, argparse, sys
3:
4: TASK_FILE = 'tasks.json'
5:
6: def load():
7:     if not os.path.exists(TASK_FILE):
8:         return []
9:     with open(TASK_FILE) as f:
10:         return json.load(f)
11:
12: def save(tasks):
13:     with open(TASK_FILE, 'w') as f:
14:         json.dump(tasks, f, indent=2)
15:
16: def next_id(tasks):
17:     return max((t['id'] for t in tasks), default=0)+1
18:
19: def add(desc):
20:     tasks=load()
21:     tasks.append({'id':next_id(tasks),'desc':desc,'done':False})
22:     save(tasks)
23:     print('Added task.')
24:
25: def list():
26:     tasks=load()
27:     for t in tasks:
28:         status='✓' if t['done'] else '✗'
29:         print(f"{t['id']}. [{status}] {t['desc']}")
30:
31: def done(id):
32:     tasks=load()
33:     for t in tasks:
34:         if t['id']==id:
35:             t['done']=True
36:             save(tasks)
37:             print('Marked done.')
38:             return
39:     print('Task not found.')
40:
41: def delete(id):
42:     tasks=load()
43:     new=[t for t in tasks if t['id']!=id]
44:     if len(new)==len(tasks):
45:         print('Task not found.')
46:         return
47:     save(new)
48:     print('Deleted.')
49:
50: def main():
51:     parser=argparse.ArgumentParser()
52:     sub=parser.add_subparsers(dest='cmd')
53:     sub.add_parser('add', help='Add a task').add_argument('desc')
54:     sub.add_parser('list', help='List tasks')
55:     sub.add_parser('done', help='Mark task done').add_argument('id', type=int)
56:     sub.add_parser('del', help='Delete task').add_argument('id', type=int)
57:     args=parser.parse_args()
58:     if args.cmd=='add': add(args.desc)
59:     elif args.cmd=='list': list()
60:     elif args.cmd=='done': done(args.id)
61:     elif args.cmd=='del': delete(args.id)
62:     else: parser.print_help()
63:
64: if __name__=='__main__':
65:     main()

Line 65 is too many. We have 65 lines. Need below 60. Let's reduce lines.

We might remove 'sys' import. Remove empty lines. Use single line for list function maybe.

Also we used sys import but not used. So remove sys. Let's recalc.

Remove import sys line 2: "import os, json, argparse". Now we have fewer lines.

We can also combine load and save lines.

Also reduce comments.

We can collapse some lines: e.g., def load: if not exists return []; else return... but we can keep.

We need to reduce total to <=60 lines.

Let's rewrite with fewer lines, removing empty lines.

Potential line count:

1: """Simple terminal task manager."""
2: import os, json, argparse
3: TASK_FILE='tasks.json'
4:
5: def load():
6:     return json.load(open(TASK_FILE)) if os.path