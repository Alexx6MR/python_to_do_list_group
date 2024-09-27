import pyinputplus # type: ignore
import time, sys

class listItem:
    def __init__(self, text: str, completed: bool = False) -> None:
        self.text = text
        self.completed = completed



class ToDoList:
    def __init__(self):
        self.current_tasks: list = []

    def showTasks(self):
        for index, tasks in enumerate(self.current_tasks):
            print(index, tasks)

    def addTasks(self):
        print("Enter what task you want to add")
        addTask = pyinputplus.inputStr()
        self.current_tasks.append(addTask)
        print("Do you want to add another task? Y/N: ")
        add_continue = pyinputplus.inputYesNo()

    def completed_task(self, task: listItem):
        marked_completed: int = pyinputplus.inputInt()
        self.current_tasks[marked_completed] = self.current_tasks[marked_completed] + ": COMPLETED"
        print("Have you completed another task? Y/N: ")
        completed_continue = pyinputplus.inputYesNo()

    def update_task(self):
        updated_task = pyinputplus.inputInt()
        print("What do you want to change? ")
        changed_task = pyinputplus.inputStr()
        self.current_tasks[updated_task] = changed_task
        print("Do you want to update another task? Y/N: ")
        update_continue = pyinputplus.inputYesNo()

    def removeTasks(self):
        remove_task = pyinputplus.inputInt()
        self.current_tasks.pop(remove_task)
        print("Do you want to remove another task? Y/N: ")
        remove_continue = pyinputplus.inputYesNo()

    def saveTasks(self, save_task: list[listItem]):
        pass
