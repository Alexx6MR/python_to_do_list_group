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
    def set_user(self, user_id:int, user_name:str)->None:
        self.user_id = user_id
        self.user_name = user_name
               
        
        
        
    #* Other Funktions
        
    def Login(self, username:str, password:str)->None:
        logged_user: dict = self.databas.login_user(username=username, password=password)
        if(logged_user == 404):    
            return 404
        else:
            self.set_user(user_id=logged_user["id"], user_name=logged_user["username"])
            return logged_user
           
        
    #* Register
    def Register(self,  username:str, password:str)->None:
        register_user: int = self.databas.register_user(username=username, password=password)
        if(register_user == 404):
            print("**It seems like this account is already registered, do you want to log in?**")
            return 404
        else:
            print()
            print(f"---User {username} successfully registered---")
            return register_user
           
                
    
                