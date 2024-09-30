import sys
from src.todo_list import ToDoList
from src.user_interface import UI
from src.Databas import DatabasManager
from src.user import User

todo_list = ToDoList()
interface = UI()
databas = DatabasManager()
current_user = User()

#* Make the program to finish and print a message
def ExitGame()->None:
   print()
   print("The program is closing")
   print("See you soon!!!!! ")
   print()
   sys.exit(0)


def LogOut()->None:
    print()
    print("!!!The Session is close!!!")
    print()
    main()
   
   
   
#* Login In 
def LogIn()->None:
    print("")
    print("**Sign In**")
    print("**Please introduce your userName and Password**")
        
    while True:
        user_input: dict = interface.input_menu()
        logged_user: dict = databas.login_user(username=user_input["username"], password=user_input["password"])
                
        if(logged_user == None):            
            print("**It seems that you dont have an account, do you want to register?**")
            interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
                {"title": "Sign Up for free", "action":Register},
                {"title": "Try again", "action":LogIn},
                {"title": "Exit", "action":ExitGame},

            ])
        current_user.set_user(user_id=logged_user["id"], user_name=logged_user["username"])
        print("")
        print("***Welcome***")            
        Menu()

#* Register
def Register()->None:
    
    print("")
    print("**Sign Up**")
    print("**Please introduce your userName and Password**")
        
    while True:
        user_input: dict = interface.input_menu()
        res_status: int = databas.register_user(username=user_input["username"], password=user_input["password"])
        if(res_status == 201):
            print(f"Welcome {user_input["username"]}")
            LogIn()
            break
        elif res_status == 403:
            print("**It seems like this account is already registered, do you want to log in?**")
            interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
               {"title": "Login to Your To do list", "action":LogIn},
               {"title": "Exit", "action":ExitGame},

            ])


def Menu()->None:
    interface.MenuUI(userInputText="Select a number: ", 
        menuOptions=[
            {"title": "Add Task", "action":AddTaskScreen},
            {"title": "Show Task", "action":ShowTaskScreen},
            {"title": "Remove Task", "action":RemoveTaskScreen},
            {"title": "Update Task", "action":UpdateTaskScreen},
            {"title": "log Out", "action":LogOut},
])





def AddTaskScreen()->None:
    print()
    print("**Welcome please add a new task**")
    user_input: str = UI.input_field(message="Add new task: ")
    todo_list.add_tasks(task=user_input, user_id=current_user.user_id)
  
    Menu()
    


def ShowTaskScreen()->None:
    print()
    print("**Here are all the tasks**")
    print()
    
    todo_list.show_tasks(user_id=current_user.user_id)
    
    interface.MenuUI(userInputText="Select a number: ", 
        menuOptions=[
        {"title": "Add Task", "action":AddTaskScreen},
        {"title": "Remove Task", "action":RemoveTaskScreen},
        {"title": "Update Task", "action":UpdateTaskScreen},
        {"title": "Log out", "action":LogOut},
    ])
    
    
    
    

def RemoveTaskScreen()->None:
    task_list:list = todo_list.get_tasks(user_id=current_user.user_id)
    
    interface.Not_task(route=Menu, task_list=task_list, message="----You dont have task to Remove ---")
  
    print()
    print("**Here can you remove one task**")
    print("_________")
    user_input: int = UI.input_field(is_text=False, message="Select Task to remove: ")
    
    todo_list.remove_tasks(task_id=user_input, user_id=current_user.user_id)
    
    interface.MenuUI(userInputText="Select a number: ", 
    menuOptions=[
        {"title": "Remove other task", "action":RemoveTaskScreen},
        {"title": "Go back", "action":Menu},
    ])

 


def UpdateTaskScreen()->None:
    task_list:list = todo_list.get_tasks(user_id=current_user.user_id)
    
    interface.Not_task(route=Menu, task_list=task_list, message="----You dont have task to Update ---")
        
    print()
    print("**Here you can Updated one task**")
    
    def ChangeStatus()->None:
        todo_list.show_tasks(user_id=current_user.user_id)
        print("_________")
        user_input: int = UI.input_field(is_text=False, message="What task is done: ")        
        todo_list.completed_task(task_id=user_input, user_id=current_user.user_id)
        interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
                {"title": "Change Status", "action":ChangeStatus},
                {"title": "Update Task", "action":UpdateTask},
                {"title": "Go back", "action":Menu},
            ])
    
    def UpdateTask()->None:
        todo_list.show_tasks(user_id=current_user.user_id)
        print("_________")
        user_input: int = UI.input_field(is_text=False, message="Select a task to change: ")        
        newTask: int = UI.input_field(message="what is the new task: ") 
        
        todo_list.update_task(task_id=user_input, user_id=current_user.user_id, task=newTask )
        interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
                {"title": "Change Status", "action":ChangeStatus},
                {"title": "Update Task", "action":UpdateTask},
                {"title": "Go back", "action":Menu},
            ])
    
    interface.MenuUI(userInputText="Select a number: ", 
        menuOptions=[
        {"title": "Change Status", "action":ChangeStatus},
        {"title": "Update Task", "action":UpdateTask},
        {"title": "Go back", "action":Menu},
    ])
    
    


def main():
   print("")
   print("**Welcome to Your To do list**")
        
   print("---In this interface you have to select a number to do something!---")

   #* Main Menu to Controll the Game
   interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
               {"title": "Login to Your To do list", "action":LogIn},
               {"title": "Sign UP for free", "action":Register},
               {"title": "Exit the Game", "action":ExitGame},

        ])



if __name__ == "__main__":
    main()