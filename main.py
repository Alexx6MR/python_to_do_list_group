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

#* Function to send a message when the user wants to end the session
def LogOut()->None:
    print()
    print("!!!The Session is close!!!")
    print()
    main()
   
#* Simulation of a login screen
def LoginScreen()->None:
    current_user.Login()
    print("")
    print("***Welcome***")            
    Menu()    

#* Simulation of a Register screen
def RegisterScreen()->None:
    current_user.Register()
    LoginScreen()

#* Menu to handle all the "pages"
def Menu()->None:
    interface.MenuUI(userInputText="Select a number: ", 
        menuOptions=[
            {"title": "Add Task", "action":AddTaskScreen},
            {"title": "Show Task", "action":ShowTaskScreen},
            {"title": "Remove Task", "action":RemoveTaskScreen},
            {"title": "Update Task", "action":UpdateTaskScreen},
            {"title": "log Out", "action":LogOut},
])

#* Simulation of a Add Task screen
def AddTaskScreen()->None:
    print()
    print("**Welcome please add a new task**")
    user_input: str = UI.input_field(message="Add new task: ")
    todo_list.add_tasks(task=user_input, user_id=current_user.user_id)
    Menu()
    
#* Simulation of a Show Task screen
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
    
#* Simulation of a Remove Task screen
def RemoveTaskScreen()->None:
    todo_list.show_tasks(user_id=current_user.user_id)
    print()
    print("**Here can you remove one task**")
    print("_________")
    user_input: int = UI.input_field(is_text=False, message="Select The Task ID to remove: ")
    
    todo_list.remove_tasks(task_id=user_input, user_id=current_user.user_id)
    
    interface.MenuUI(userInputText="Select a number: ", 
    menuOptions=[
        {"title": "Remove other task", "action":RemoveTaskScreen},
        {"title": "Go back", "action":Menu},
    ])

#* Simulation of a Update Task screen
def UpdateTaskScreen()->None:
    todo_list.show_tasks(user_id=current_user.user_id)
        
    print()
    print("**Select the id to update the task**")
    
    def ChangeStatus()->None:
        todo_list.show_tasks(user_id=current_user.user_id)
        print("_________")
        user_input: int = UI.input_field(is_text=False, message="Select The Task Id to Change: ")        
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
    

#* App Entry Point 
def main():
   print("")
   print("**Welcome to Your To do list**")
        
   print("---In this interface you have to select a number to do something!---")

   #* Main Menu to Controll the Game
   interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
               {"title": "Login to Your To do list", "action":LoginScreen},
               {"title": "Register for free", "action":RegisterScreen},
               {"title": "Exit", "action":ExitGame},

        ])



if __name__ == "__main__":
    main()