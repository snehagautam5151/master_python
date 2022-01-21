# name: mr. McNally
# date: 2021-08-25
# descrition: Text-based space advanteage game

import random
import time

def displayIntro():
    print("its the end of a long year of lighting space criminals")
    print("you come to crossroads on your trip home, one path leads home")
    print("where you will be handsomply rewarded fro a job well done")
    print("and the others leads through a gamma ray burst that will disentigrate yoy")
    print()
    
def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("which path will you choose? (1 or 2): ")
        
    return path 

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteriod ")
    time.sleep(2)
    print("But yours skin begins to tingle...")
    print()
    time.sleep(2)
    
    correctPath = random.randint(1,2)
    
    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admission from the citizens of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass throuh you")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of ")
        
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
        
    displayIntro() 
    choice = choosePath()
    checkPath(choice)   #  choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
   
