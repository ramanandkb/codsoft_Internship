#To-Do list
# Define an empty list to store tasks
tasks = []


# Function to display the to-do list
def show_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")


# Function to add a task to the list
def add_task(task):
  tasks.append(task)
  print(f"Added: {task}")


# Function to mark a task as completed
def complete_task(index):
  if tasks and 1 <= index <= len(tasks):
    task = tasks.pop(index - 1)
    print(f"Completed: {task}")
  else:
    print("Invalid task number. Please try again.")


# Function to remove a task from the list
def remove_task(index):
  if tasks and 1 <= index <= len(tasks):
    task = tasks.pop(index - 1)
    print(f"Removed: {task}")
  else:
    print("Invalid task number. Please try again.")

# Main program loop
while True:
  print("\nOptions:")
  print("1. Show To-Do List")
  print("2. Add Task")
  print("3. Complete Task")
  print("4. Remove Task")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    show_tasks()
  elif choice == "2":
    show_tasks()
    task = input("Enter the task: ")
    add_task(task)
  elif choice == "3":
    show_tasks()
    if tasks:
      index = int(input("Enter the task number to mark as completed: "))
      complete_task(index)
  elif choice == "4":
    show_tasks()
    if  tasks:
      index = int(input("Enter the task number to remove: "))
      remove_task(index)
  elif choice == "5":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
