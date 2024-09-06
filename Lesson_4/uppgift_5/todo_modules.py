# Suggestion: Clean up printing of todo list
# Suggestion: serach task list for existing duplicates using task key-value pair
def add_task(todo_list:list):
  new_task = input("Add new task: ")
  task_entry = {"task": new_task, "task done": False}
  todo_list.append(task_entry)
  return todo_list

# Intead of tying a unique id to each task this will run after each operation that modifies the list to update the id values 
# This is done so that users can select the tasks using the id number
def enumerate_tasks(todo_list:list):
  loop_counter= 0
  if len(todo_list) > 0:
    for item in todo_list:
      loop_counter += 1
      item["id"] = loop_counter
  return todo_list

def toggle_done(todo_list:list):
  print(todo_list)
  task_id = int(input("Enter the task you want to mark as done: "))
  for task in todo_list:
    if task["id"] == task_id:
      task["task done"] = not task["task done"] #Toggles the boolean to the opposite of the existing value True->False, False->True
  return todo_list

def clear_done_tasks(todo_list:list):
  for task in todo_list:
    if task["task done"] == True:
      todo_list.remove(task)
  return todo_list

def remove_task(todo_list:list):
  print(todo_list)
  task_id = int(input("Enter the task you want to remove: "))
  for task in todo_list:
    if task["id"] == task_id:
      todo_list.remove(task)
  return todo_list

def list_tasks(todo_list:list):
  print(todo_list)