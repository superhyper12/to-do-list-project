class Task:
    def __init__(self, name, priority, dueDate):
        self.name = name 
        self.priority = priority
        self.dueDate = dueDate
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self):
        print('Enter task')
        name = input('enter task name: ')
        priority = input('enter low, medium, high priority: ')
        dueDate = input('enter due date (ex: 01-02-2024): ')
        self.tasks.append(Task(name,priority,dueDate))
        print("Task added!")
    
    def delete_task(self):
        print("Which one of the tasks you want to delete?")
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i].name}")
        user_input = input("Enter task Number: ")
        if 0 <= user_input <= len(self.task):
            self.tasks.remove(self.tasks[int(user_input)-1])
            print("Task removed!")
        else:
            print("invalid task number, please enter the number from the list")

    def edit_task(self):
        print("which one of the tasks you want to edit?")
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i].name}")
        user_input = input("Enter task Number: ")

        selected_task_index = int(user_input) - 1
        select_task = self.tasks[selected_task_index]

        editProperties = int(input("which part of the task would you like to edit? (1) name (2) priority (3) due date: "))

        if editProperties == 1:
            user_changes = input("Enter name change: ")
            select_task.name = user_changes
            print("name changed")

        elif editProperties == 2:
            user_changes2 = input("Enter priority change: ")
            select_task.priority = user_changes2
            print("priority changed")

        elif editProperties == 3:
            user_changes3 = input("Enter due date change:  ")
            select_task.dueDate = user_changes3
            print("due date changed")
        else:
            print("invalid choices. please enter a number from the choice given: ")


            
    def get_all_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.name} Priority: {task.priority} Due Date: {task.dueDate}")
        




def main():
    task_manager = TaskManager()
    while True:
        main_choice = int(input("(0) exit (1) add task (2) edit task (3) get all task: "))
        if main_choice == 0:
            break
        elif 1 <= main_choice <= 3:
                getattr(task_manager, f"add_task" if main_choice == 1 else f"edit_task" if main_choice == 2 else "get_all_tasks")()
        else:
            print("invalid choice. Please enter a number from 1 to 3. ")


main()
        




