from src.databas import DatabasManager



class ToDoList:
    def __init__(self):
        self.current_tasks: list = []
        self.databas = DatabasManager()
        
    #* Takes a task submitted by the user and sends it to the database
    def add_tasks(self, user_id:int, task:str):
        self.databas.add_tasks(user_id=user_id, task=task)
        print()
        print("---The task was created successfully---")
    
    
    #* Gets all tasks from the database and returns them to the user
    def get_tasks(self, user_id:int)-> list:
        return self.databas.get_tasks(user_id=user_id)


    #* Gets the old task, generates the change and then returns both tasks, the new and the old one
    def completed_task(self, task_id: int, user_id:int):
        old_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)

        if(old_task["Status"] == 0):
            self.databas.update_status(status=1, task_id=task_id, user_id=user_id)
            new_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
            print()
            print("---The task status changed successfully---")
            return [old_task, new_task]
        else:
            self.databas.update_status(status=0, task_id=task_id, user_id=user_id)
            new_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
            print()
            print("---The task status changed successfully---")
            return [old_task, new_task]
        
        
    #* Update a task
    def update_task(self, task_id: int, user_id:int, task:str):
        old_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
        self.databas.update_task(task_id=task_id, task=task, user_id=user_id)
        new_task: dict = self.databas.get_one_task(task_id=task_id, user_id=user_id)
        print()
        print("---The task changed successfully---")
        return [old_task, new_task]

    
    #* Remove a task
    def remove_tasks(self, task_id:int, user_id):
        task_exist = self.databas.get_one_task(task_id=task_id, user_id=user_id)
        if(task_exist):
            self.databas.remove_task(task_id=task_id, user_id=user_id)
            print()
            print("---Task removed succesfully---")
        else:
            print("Sorry but that task do not exist")

    

    
    
        