import json

def manage_task(task):
    with open('tasks.txt', 'w') as f:
        json.dump(task, f, indent=4)

def save_task():
    try:
        with open('tasks.txt', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
