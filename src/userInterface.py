import pyinputplus as pyip

class IMenuOption:
    def __init__(self, title: str, action) -> None:
        self.title = title
        self.action = action

class UI:
    def __init__(self) -> None:
        pass
    

    #* This is the Menu that let the users take a decision.
    def MenuUI(self, menuOptions:list[IMenuOption]=[], userInputText: str = "")->None:
        optionLength:int = len(menuOptions)
    
        print()
        print("_______Menu_____")
        print()
    
        #* Loop to print all the title from the option dictionary in order
        for item in range(optionLength):
            option:IMenuOption = menuOptions[item]
            print(f"{item + 1}. {option.title}")


        #* Input to choose a option Obs: I use pyinputplus for validation
        print("_________________")
        userInput:int = pyip.inputNum(userInputText, max=optionLength, min=1)    
        
        
        #* Loop to print and run the action in the selected object
        for item in range(optionLength):
            option:IMenuOption = menuOptions[item]
            if(userInput == item + 1):
                #* this is to run the option function
                option.action()

    
