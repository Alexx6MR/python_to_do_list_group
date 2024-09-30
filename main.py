import sys
from src.todo_list import ToDoList
from src.user_interface import UI
from src.user import User

todo_list = ToDoList()
interface = UI()
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
def LoginScreen()->None:
    current_user.Login()
    print("")
    print("***Welcome***")            
    Menu()    

#* Register
def RegisterScreen()->None:
    current_user.Register()
    LoginScreen()



#* Menu to handle all the pages (AUTH)
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
               {"title": "Login to Your To do list", "action":LoginScreen},
               {"title": "Sign UP for free", "action":RegisterScreen},
               {"title": "Exit the Game", "action":ExitGame},

        ])



if __name__ == "__main__":
    main()