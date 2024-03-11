import random

class CuteToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Task added!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("(｡♥‿♥｡) Task removed!")
        else:
            print("(ﾉಥ益ಥ)ﾉ Sorry, couldn't find that task!")

    def display_tasks(self):
        print("\n┏(*^‿^*)┛ Here's your cute to-do list:┗(´∩｡• ᵕ •｡∩) ┓")
        if self.tasks:
            for i, task in enumerate(self.tasks, start=1):
                print(f"  ✿ {i}. {task}")
        else:
            print("(◕︿◕✿) Your to-do list is empty!")

    def random_encouragement(self):
        encouragements = [
            "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ You're doing great!",
            "(っ˘ڡ˘ς) Keep up the good work!",
            "(｡♥‿♥｡) You got this!",
            "(ᴗ˳ᴗ) Stay motivated!",
            "(✿◠‿◠) You're awesome!",
            "(ﾉ≧∀≦)ﾉ Keep shining!",
            "(⊃｡•́‿•̀｡)⊃ You're amazing!",
            "(∩˃o˂∩)♡ You're fantastic!",
            "(ﾉ´ヮ`)ﾉ*: ･ﾟ You're unstoppable!",
            "(∩^o^)⊃━☆ﾟ.*･｡ﾟ Keep going!"
        ]
        print(random.choice(encouragements))

# Example usage:
if __name__ == "__main__":
    todo_list = CuteToDoList()

    while True:
        print("\n*:・ﾟ✧Cute To-Do List Menu *:・ﾟ✧")
        print("1 ♥ Add Task")
        print("2 ♥ Remove Task")
        print("3 ♥ Display Tasks")
        print("4 ♥ Get Random Encouragement")
        print("5 ♥ Exit")

        choice = input("\nଘ(੭ˊᵕˋ)੭* ੈ✩‧₊ Enter your choice: ")
        if choice == '1':
            task = input("ʕ·ᴥ·ʔ Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("(=^‥^=) Enter the task to remove: ")
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
