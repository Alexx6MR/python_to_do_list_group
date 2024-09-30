


class User: 
    def __init__(self):
        self.user_id: int
        self.user_name: str
        self.task_list: list = []
        
        
    
    def set_task_list(self, tasks_list:list[dict])->None:

       self.task_list.append(tasks_list)
    
    def set_one_task(self, task:dict) ->None:
        self.task_list.append(dict(task))
    
    def set_user(self, user_id:int, user_name:str)->None:
        self.user_id = user_id
        self.user_name = user_name
       
    #* Getters
        
        
    def get_all_task(self,)->list:
        return self.task_list
        
        
    def get_user_info(self)->list:
        return dict(user_id=self.user_id, user_name=self.user_name, task_list=self.task_list)
        
        
        
        
