"""Terminal task manager: add, list, complete, delete tasks."""
import json, os, sys, argparse

FILE = "tasks.json"

def load(): 
    if not os.path.exists(FILE): return []
    with open(FILE) as f: return json.load(f)

def save(t): 
    with open(FILE,"w") as f: json.dump(t,f,indent=2)

def list_tasks(t): 
    for i,a in enumerate(t,1): 
        s='[x]' if a['done'] else '[ ]'
        print(f"{i}. {s} {a['desc']}")

def main(): 
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='cmd')
    sub.add_parser('list')
    sub.add_parser('add').add_argument('desc')
    sub.add_parser('done').add_argument('id',type=int)
    sub.add_parser('del').add_argument('id',type=int)
    ns=p.parse_args()
    tasks=load()
    if ns.cmd=='list':
        list_tasks(tasks)
    elif ns.cmd=='add':
        tasks.append({'desc':ns.desc,'done':False});save(tasks)
    elif ns.cmd=='done':
        if 1<=ns.id<=len(tasks):tasks[ns.id-1]['done']=True;save(tasks)
    elif ns.cmd=='del':
        if 1<=ns.id<=len(tasks):tasks.pop(ns.id-1);save(tasks)
    else:
        p.print_help()

if __name__=='__main__': main()