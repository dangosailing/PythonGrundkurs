def add_todo(todo_list:list):
  new_task = input("Add new task: ")
  task_entry = {"task": new_task, "task done": False}
  todo_list.append(task_entry)
  return todo_list