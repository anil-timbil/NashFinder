## Main Program
## 10.10.2019
## Anil Timbil, Sean King
## This program creates a menu we can use to utilize the functionalities described
## in this project. The program takes an inputfile name and performs the indicated
## functionality.

from Game import *

def main():
    filename = input("Please input the name of the file that you want to test: ") #get inputfile
    new_Game = Game(filename)
    exit = False
    while not exit:
        print("Do you want to test for (A) pure Nash equilibria or (B) mixed Nash equilibria")
        choice = input("(C) Find dominant strategies, (D) Find dominated strategies?  Or, type exit to end the program.")
        if choice.lower() == "a":
            print(new_Game.findPureNash())
        elif choice.lower() == "b":
            q,p=new_Game.findMixedNash()
            print("mixed nash: ", q,p)
        elif choice.lower() == "c":
            new_Game.findDominant()
        elif choice.lower() == "d":
            new_game.findDominated()
        elif choice.lower() == "exit":
            exit = True

main()
