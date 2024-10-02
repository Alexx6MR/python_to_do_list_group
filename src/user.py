from src.databas import DatabasManager
from src.user_interface import UI

class User: 
    def __init__(self):
        self.user_id: int
        self.user_name: str
        self.user_taskId: int
        self.task_list: list = []
        self.databas = DatabasManager()
        self.interface = UI()
    
    
    
    #* Setters
    
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
        
        
        
        
    #* Other Funktions
        
    def Login(self, username:str, password:str)->None:
        logged_user: dict = self.databas.login_user(username=username, password=password)
        if(logged_user is None):    
            return None
        else:
            self.set_user(user_id=logged_user["id"], user_name=logged_user["username"])
            return logged_user
           
        
    #* Register
    def Register(self,  username:str, password:str)->None:
        register_user: int = self.databas.register_user(username=username, password=password)
        if(register_user is None):
            return None
        else:
            return register_user
           
                
    
                