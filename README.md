
# Cute To-Do List Documentation

## Introduction
The Cute To-Do List is a simple Python program designed to help users manage their tasks in a fun and visually appealing way. With cute kaomoji (Japanese emoticons) responses and encouraging messages, this program aims to make task management a delightful experience.

## Features
1. **Add Task**: Users can add tasks to their to-do list.
2. **Remove Task**: Users can remove tasks from their to-do list.
3. **Display Tasks**: Users can view their current tasks.
4. **Get Random Encouragement**: Users receive random encouraging messages to boost their motivation.
5. **Exit**: Users can exit the program.

## Usage
1. **Add Task**: Enter option `1` from the menu and input the task you want to add when prompted.
2. **Remove Task**: Enter option `2` from the menu and input the task you want to remove when prompted.
3. **Display Tasks**: Enter option `3` from the menu to view your current tasks.
4. **Get Random Encouragement**: Enter option `4` from the menu to receive a random encouraging message.
5. **Exit**: Enter option `5` from the menu to exit the program.

## Installation
1. Clone the repository from GitHub: `git clone https://github.com/your/repository.git`
2. Navigate to the directory: `cd cute-to-do-list`
3. Run the Python script: `python cute_to_do_list.py`

## Requirements
- Python 3.x

## Example
```python
from cute_to_do_list import CuteToDoList

# Create a CuteToDoList object
todo_list = CuteToDoList()

# Display the menu and interact with the to-do list
while True:
    print("\n┏(＾0＾)┛ Cute To-Do List Menu ┗(＾0＾) ┓")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Get Random Encouragement")
    print("5. Exit")

    choice = input("\nEnter your choice: ")
    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        todo_list.remove_task(task)
    elif choice == '3':
        todo_list.display_tasks()
    elif choice == '4':
        todo_list.random_encouragement()
    elif choice == '5':
        print("(｡♥‿♥｡) Bye bye! Take care!")
        break
    else:
        print("(⊙_☉) Invalid choice. Please select a valid option.")
