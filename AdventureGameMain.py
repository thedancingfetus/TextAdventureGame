import sys
import os

weapon = False
retry = True

def introscene():
    directions = ["left","right","forward"]
    print("You are at a crossroads, and you can choose to go down and of the four hallways. Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: left/right/backward/forward")
        userinput = input()
        if userinput == "left":
            showShadowFigure()
        elif userinput == "right":
            showSkeletons()
        elif userinput == "forward":
            hauntedRoom()
        elif userinput == "backward":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")

def showShadowFigure():
    directions = ["right","backward"]
    print("You see a dark, shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: right/left/backward")
        userinput = input()
        if userinput == "right":
            camerascene()
        elif userinput == "left":
            print("You find that this door opens into a wall.")
        elif userinput == "backward":
            introscene()
        else:
            print("Please enter a valid option.")

def camerascene():
    directions = ["forward","backward"]
    print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: forward/backward")
        userinput = input()
        if userinput == "forward":
            print("You've made it! You've found an exit!")
            restart_program()
        elif userinput == "backward":
            showShadowFigure()
        else:
            print("Please enter a valid option.")

def hauntedRoom():
    directions = ["right","left","backward"]
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: right/left/backward")
        userinput = input()
        if userinput == "right":
            print("Multiple ghoul-like creatures start emerging as you enter the room. You are killed. You have expired. You have ceased to be.")
            restart_program()
        elif userinput == "left":
            print("You made it! You've found an exit!")
            restart_program()
        elif userinput == "backward":
            introscene()
        else:
            print("Please enter a valid option.")

def showSkeletons():
    directions = ["backward","forward"]
    global weapon
    print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Options: left/backward/forward")
        userinput = input()
        if userinput == "left":
            print("You find that this door opens into a wall. You notice a loose stone, so you move it and discover a knife.")
            weapon = True
        elif userinput == "backward":
            introscene()
        elif userinput == "forward":
            strangeCreature()
        else:
            print("Please enter a valid option.")

def strangeCreature():
    actions = ["fight","flee"]
    global weapon
    print("A strange, ghoul-like creature has appeared. You can either run or fight it. What would you like to do?")
    userinput = ""
    while userinput not in actions:
        print("Options: flee/fight")
        userinput = input()
        if userinput == "fight":
            if weapon:
                print("You kill the ghoul with the knife you found earlier. After moving forward, you find one of the exits. You made it!")
                restart_program()
            else:
                print("The creature has kill.")
                restart_program()
        elif userinput == "flee":
                showSkeletons()
        else:
            print("Please enter a valid option.")

def restart_program():
    global retry
    print("Would you like to retry?[Y/N]")
    if input() == "Y":
        retry = True
    else:
        retry = False

if __name__ == "__main__":
    while retry:
        print("Welcome to the Adventure Game!")
        print("As an avid traveler, you have decided to visit the Catacombs of Paris")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: [Type 'quit' to Quit]")
        name = input()
        if(name != "quit"):                   
            print("Good luck, "+name+".")
            introscene()
        else:
            quit()