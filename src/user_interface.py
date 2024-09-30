import pyinputplus as pyip


class UI:
    def __init__(self) -> None:
        pass
    

    #* This is the Menu that let the users take a decision.
    def MenuUI(self, menuOptions:list[dict]=[], userInputText: str = "")->None:
        optionLength:int = len(menuOptions)
    
        print()
        print("_______Menu_____")
        print()
    
        #* Loop to print all the title from the option dictionary in order
        for item in range(optionLength):
            option:dict = menuOptions[item]
            print(f"{item + 1}. {option["title"]}")


        #* Input to choose a option Obs: I use pyinputplus for validation
        print("_________________")
        userInput:int = pyip.inputNum(userInputText, max=optionLength, min=1)    
        
        
        #* Loop to print and run the action in the selected object
        for item in range(optionLength):
            option:dict = menuOptions[item]
            if(userInput == item + 1):
                #* this is to run the option function
                option["action"]()

    
    def input_menu(self)->dict:
         #* Input to choose a option Obs: I use pyinputplus for validation
         #* UserName input
        print("_________________")
        user_name_input:str = pyip.inputStr("Username: ")  
        
        #* Password input
        print("_________________")
        user_password_input:str = pyip.inputStr("Password: ") 
        
        return dict(username=user_name_input.lower(), password=user_password_input.lower())
    
    
    def input_field(message:str, is_text:bool=True)->str:
        print("_________________")
        if(is_text):
          return pyip.inputStr(message)  
        else:
           return pyip.inputNum(message) 
    
    
    def Not_task(self, task_list:list, route:callable, message:str):
        if len(task_list) <= 0:
            print()
            print(message)
            self.MenuUI(userInputText="Select a number: ", 
                menuOptions=[
                {"title": "Go back", "action":route},
            ])