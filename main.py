import sys
from src.todo_list import ToDoList
from src.user_interface import UI
from src.user import User

todo_list = ToDoList()
interface = UI()
current_user = User()

#* Make the program to finish and print a message
def exit()->None:
   print()
   print("The program is closing")
   print("See you soon!!!!! ")
   print()
   sys.exit(0)

#* Function to send a message when the user wants to end the session
def logout()->None:
    print()
    print("!!!The Session is close!!!")
    print()
    main()
   
#* Simulation of a login screen
def login_screen()->None:
    print("")
    print("**LOGIN SCREEN**")
    print("**Please introduce your Username and Password**")
    
    while True:
        user_input: dict = interface.input_menu()
        logged_user:dict = current_user.Login(username=user_input["username"], password=user_input["password"])
        
        if(logged_user == None):    
            print("**It seems that you dont have an account, do you want to register?**")
            interface.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                    {"title": "Register for free", "action":register_screen},
                    {"title": "Try again", "action":login_screen},
                ])
        else:
            print("")
            print(f"***Welcome {logged_user["username"]}***")            
            Menu()    

#* Simulation of a Register screen
def register_screen()->None:
    print("")
    print("**REGISTER SCREEN**")
    print("**Please introduce your Username and Password**")
    while True:
        user_input: dict = interface.input_menu()
        res = current_user.Register(username=user_input["username"], password=user_input["password"])
        
        if(res == 403):
            print("**It seems like this account is already registered, do you want to log in?**")
            interface.MenuUI(
                menu_title="error trying to register a user",
                userInputText="Select a number: ", 
                menuOptions=[
                {"title": "Try again", "action":register_screen},
                {"title": "Log in", "action":login_screen},
            ])
        else:
            main()



#* Menu to handle all the "pages"
def Menu()->None:
    interface.MenuUI(
        menu_title="Navigaiton Menu",
        userInputText="Select a number: ", 
        menuOptions=[
            {"title": "Add Task", "action":add_task_screen},
            {"title": "Show Task", "action":show_task_screen},
            {"title": "Remove Task", "action":remove_task_screen},
            {"title": "Update Task", "action":update_task_screen},
            {"title": "log Out", "action":logout},
])

#* Simulation of a Add Task screen
def add_task_screen()->None:
    print()
    print("**CREATE TASK SCREEN**")
    print("**Welcome and please add a new task**")
    all_task: list[dict] = todo_list.get_tasks(user_id=current_user.user_id)
    interface.show_tasks(task_list=all_task)
    user_input: str = UI.input_field(message="Add new task: ")
    todo_list.add_tasks(task=user_input, user_id=current_user.user_id)
    Menu()
    
#* Simulation of a Show Task screen
def show_task_screen()->None:
    print()
    print("**SHOW SCREEN**")
    print("**Here are all the tasks**")
    print()
    all_task: list[dict] = todo_list.get_tasks(user_id=current_user.user_id)
    interface.show_tasks(task_list=all_task)
    
    interface.MenuUI(
        menu_title= "Show task list Menu",
        userInputText="Select a number: ", 
        menuOptions=[
        {"title": "Add Task", "action":add_task_screen},
        {"title": "Remove Task", "action":remove_task_screen},
        {"title": "Update Task", "action":update_task_screen},
        {"title": "Log out", "action":logout},
    ])
    
#* Simulation of a Remove Task screen
def remove_task_screen()->None:
    print()
    print("**REMOVE SCREEN**")
    print("**Here you can remove one task**")
    all_task: list[dict] = todo_list.get_tasks(user_id=current_user.user_id)
    interface.show_tasks(task_list=all_task)
    
    print("_________")
    user_input: int = UI.input_field(is_text=False, message="Select The Task ID to remove it: ")
    
    todo_list.remove_tasks(task_id=user_input, user_id=current_user.user_id)
    
    interface.MenuUI(
        menu_title="Remove Task Menu",
        userInputText="Select a number: ", 
        menuOptions=[
        {"title": "Remove other task", "action":remove_task_screen},
        {"title": "Go back", "action":Menu},
    ])

#* Simulation of a Update Task screen
def update_task_screen()->None:
        
    print()
    print("**UPDATE SCREEN**")
    print("**Choose which option you want to do**")
    
    def ChangeStatus()->None:
        all_task: list[dict] = todo_list.get_tasks(user_id=current_user.user_id)
        interface.show_tasks(task_list=all_task)
        print("_________")
        user_input: int = UI.input_field(is_text=False, message="Select The Task Id to Change: ")        
        [old_task, new_task] = todo_list.completed_task(task_id=user_input, user_id=current_user.user_id)
        print()
        print("Task:")
        interface.show_one_task(old_task)
        print("Change to")
        interface.show_one_task(new_task)
        interface.MenuUI(
            menu_title="Change Status Menu",
            userInputText="Select a number: ", 
            menuOptions=[
                {"title": "Change Status", "action":ChangeStatus},
                {"title": "Update Task", "action":UpdateTask},
                {"title": "Go back", "action":Menu},
            ])
    
    def UpdateTask()->None:
        all_task: list[dict] = todo_list.get_tasks(user_id=current_user.user_id)
        interface.show_tasks(task_list=all_task)
        print("_________")
        user_input: int = UI.input_field(is_text=False, message="Select a task to change: ")        
        new_taskText: str = UI.input_field(message="what is the new task: ") 
        [old_task, new_task] = todo_list.update_task(task_id=user_input, user_id=current_user.user_id, task=new_taskText)
        print()
        print("Task:")
        interface.show_one_task(old_task)
        print("Change to")
        interface.show_one_task(new_task)
        interface.MenuUI(
            menu_title="Update Task Menu",
            userInputText="Select a number: ", 
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
    

#* App Entry Point 
def main():
   print("")
   print("**Welcome to Your To do list**")
        
   print("---In this interface you have to select a number to do something!---")

   #* Main Menu to Controll the Game
   interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
               {"title": "Login to Your To do list", "action":login_screen},
               {"title": "Register for free", "action":register_screen},
               {"title": "Exit", "action":exit},

        ])



if __name__ == "__main__":
    main()