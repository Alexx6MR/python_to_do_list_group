from src.Databas import DatabasManager
from src.user_interface import UI

class User: 
    def __init__(self):
        self.user_id: int
        self.user_name: str
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
        
    def Login(self)->None:
        print("")
        print("**Sign In**")
        print("**Please introduce your userName and Password**")
        
        while True:
            user_input: dict = self.interface.input_menu()
            logged_user: dict = self.databas.login_user(username=user_input["username"], password=user_input["password"])
                
            if(logged_user == None):            
                print("**It seems that you dont have an account, do you want to register?**")
                self.interface.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                {"title": "Sign Up for free", "action":self.Register},
                {"title": "Try again", "action":self.Login},

                ])
            self.set_user(user_id=logged_user["id"], user_name=logged_user["username"])
            break
            
           
        
    #* Register
    def Register(self)->None:
    
        print("")
        print("**Sign Up**")
        print("**Please introduce your userName and Password**")
        
        while True:
            user_input: dict = self.interface.input_menu()
            res_status: int = self.databas.register_user(username=user_input["username"], password=user_input["password"])
            if(res_status == 403):
                print("**It seems like this account is already registered, do you want to log in?**")
                self.interface.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                {"title": "Try again", "action":self.Register},
                {"title": "Log in", "action":self.Login},
               

            ])
            break
                