from src.Databas import DatabasManager



class ToDoList:
    def __init__(self):
        self.current_tasks: list = []
        self.databas = DatabasManager()
        
        
        
    def add_tasks(self, user_id:int, task:str):
        last_task_id:int = self.databas.add_tasks(user_id=user_id, task=task)
        
        if(last_task_id == None):
            print("There is not a task id")
        else:
            new_task: dict = self.databas.get_one_task(task_id=last_task_id, user_id=user_id)
            print()
            if(new_task != None):
                print(f"The task {self.show_one_task(new_task)} was created successfully")
    
    
    def get_tasks(self, user_id:int)-> list:
        return self.databas.get_tasks(user_id=user_id)


    def show_one_task(self, task:dict):
        print(f"Id: {task["id"]}, Uppgift: {task["task"]}, Status: {bool(task["status"])}")


    def show_tasks(self, user_id:int) -> list:
        print("Actual task on list: ")
        print()
        task_list:list = self.get_tasks(user_id=user_id)
        if len(task_list) <= 0:
            print("----You dont have task yet---")
        else:
            for task in task_list:
                self.show_one_task(task=task)


    def completed_task(self, task_id: int, user_id:int):
        old_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)

        if(old_task["Status"] == 0):
            self.databas.update_status(status=1, task_id=task_id)
            new_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
            print(f"Task {self.show_one_task(old_task)} change to {self.show_one_task(new_task)}")
            print(f"The status has change succesfully")
        else:
            self.databas.update_status(status=0, task_id=task_id)
            new_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
            print(f"Task {self.show_one_task(old_task)} change to {self.show_one_task(new_task)}")
            print(f"The status has change succesfully")
        

    def update_task(self, task_id: int, user_id:int, task:str):
        old_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)

        self.databas.update_task(task_id=task_id, task=task)
        new_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
        print(f"Task {self.show_one_task(old_task)}")
        print(f"Change to {self.show_one_task(new_task)}")
        print(f"The status has change succesfully")


    def remove_tasks(self, task_id:int, user_id):
        task_exist = self.databas.get_one_task(task_id=task_id, user_id=user_id)
        if(task_exist):
            self.databas.remove_task(task_id=task_id, user_id=user_id)
            print(f"Task removed succesfully")
        else:
            print("Sorry but that task do not exists")

    

    
    
        