from src.userInterface import UI, IMenuOption
import sys

class TodoList:
    def __init__(self) -> None:
        self.interface = UI()
    
    #* Make the program to finish and print a message
    def ExitGame(self)->None:
        print()
        print("Thank you for Playing :) ")
        print("See you soon!!!!! ")
        print()
        sys.exit(0)
        
    
    def Start(self)->None:
        
        print("")
        print("**Welcome to 21 Games**")
        print("**I hope you know the rules if you dont please select rules and will see them**")
        
        print("---In this interface you have to select a number to do something!---")

        #* Main Menu to Controll the Game
        self.interface.MenuUI(userInputText="Select a number: ", 
            menuOptions=[
                IMenuOption(title = "Start Program", action=None),
                IMenuOption(title = "Exit Program", action=self.ExitGame)


        ])