#!usr/bin/python3
# Program Name: CRAFT MASTER
# Program Description: Material gathering and crafting game
#  by MAARTEN BERGSMA    www.bergsmaarten@gmail.com
# Python 3.5.0 program template in Guerin computer science course
# Dec 2015, Vers 2.3

import random
import time

resInv = []
craftedInv = []
toolInv = ["HANDS"]
resLeft = True
resCount = 15                      

# FUNCTIONS

# Give me space...
def giveMeSpace():
    print("\n"*40)
    return

# Check if there are resources left
def checkForRes(resCount):
    global resLeft
    if resCount <= 0:
        resLeft = False
    else:
        print("> There are",resCount,"resouces left in the forest")
    return

def letThereBeLine():
    print("\n<>==================================================<>\n")
    return

# Print out a thought sim
def ponderSec():
    time.sleep(1)
    print("-")
    time.sleep(1)
    print("-")
    time.sleep(1)
    print("-")
    time.sleep(1)
    return

# Launches the player interface
def interfaceLaunch(gatherAble,reqTool,resInv,resType,toolInv,craftedInv):
    global resCount
    while len(gatherAble) > 0:
        letThereBeLine()
        playerAction = input("  [1] CRAFT   [2] GATHER   [3] INVENTORY   [4] MOVE\n\n>> ")
        while playerAction != "1" and playerAction != "2" and playerAction != "3" and playerAction != "4":
            letThereBeLine()
            playerAction = input("> Please select...\n\n  [1] CRAFT   [2] GATHER   [3] INVENTORY   [4] MOVE\n\n>> ")
        if playerAction == "1":
            letThereBeLine()
            print("Haha, NO")
        elif playerAction == "2":
            letThereBeLine()
            if "NOTHING" in gatherAble:
                break
            if reqTool in toolInv:
                print("> Collected",gatherAble[0],"with",reqTool)
                print(">",gatherAble[0],"added to inventory")
                resInv.append(gatherAble.pop(0))
                resCount -= 1
            else:
                print("> You cannot collect",gatherAble[0])
                print("> You need to craft a(n)",reqTool,"before you can collect this resource")
        elif playerAction == "3":
            letThereBeLine()
            print("You have",len(resInv),"items:")
            for i in resInv:
                  print(i)
        elif playerAction == "4":
            letThereBeLine()
            return
        
    print("> There's nothing left to gather from this resource")
    
    gatherAble.append("NOTHING")
    interfaceLaunch(gatherAble,reqTool,resInv,resType,toolInv,craftedInv)
    return

# Game over interface
def endGame():
    letTherebeLine()
    print("> You have exhausted the resources around you")
    print("> There is still time to craft the resources you have already gathered...")
    while resLeft == False:
        letThereBeLine()
        endAction = input("  [1] CRAFT   [2] INVENTORY\n\n>> ")
        while endAction != "1" and playerAction != "2" and playerAction != "3" and playerAction != "4":
            letThereBeLine()
            playerAction = input("> Please select...\n\n  [1] CRAFT   [2] GATHER   [3] INVENTORY   [4] MOVE\n\n>> ")
        
# Contains actual game code... randomization of resources, locations, etc.
def main():
    
    global resLeft
    global resCount
    global resInv
    global craftedInv
    global toolinv
    
    # Asciing about the location
    
    letThereBeLine()
    locations = ["FOREST","MOUNTAINS","DESERT","RIVERBANK"]
    pickLocation = input("> Would you like to delegate a starting location?\n\n[Y] Yes\n[N] Choose one randomly\n\n>> ")
    while pickLocation != "Y" and pickLocation != "y" and pickLocation != "n" and pickLocation != "N":
        letThereBeLine()
        pickLocation = input("> Please select...\n\n[Y] Pick location\n[N] Choose one randomly\n\n>> ")
        
    if pickLocation == "N" or pickLocation == "n":
        # Change this later, when there are more locations...
        trueLocation = str(random.randint(1,1)) # This has GOT to be a string to work with rest of program
                           
    if pickLocation == "Y" or pickLocation == "y":
        letThereBeLine()
        trueLocation = input("> Where do you want to go?\n\n[1] Forest\n[2] Mountains\n[3] Desert\n[4] Riverbank\n\n>> ")
        while trueLocation != "1" and trueLocation != "2" and trueLocation != "3" and trueLocation != "4":
            letThereBeLine()
            trueLocation = input("> Please select:\n\n[1] Forest\n[2] Mountains\n[3] Desert\n[4] Riverbank\n\n>> ")
    giveMeSpace()
    print("   ________   __  _______  _____________   ___  ______   ")
    print("  / ___/ _ | /  |/  / __/ / __/_  __/ _ | / _ \/_  __/   ")
    print(" / (_ / __ |/ /|_/ / _/  _\ \  / / / __ |/ , _/ / /      ")
    print(" \___/_/ |_/_/  /_/___/ /___/ /_/ /_/ |_/_/|_| /_/       ")
    
                           
    # True location FOREST
    if trueLocation == "1":

        # Story introduction for FOREST
        letThereBeLine()
        time.sleep(1)
        print("> You suddenly wake up in the middle of a vast forest.")
        time.sleep(2.5)
        print("> You look around.")
        ponderSec()
        print("> There's nobody around ... only you.")
        time.sleep(2.5)
        print("> However, there are many natural resources around you.")
        time.sleep(2.5)
        print("> You realize that the only way to survive is to explore and gather.")
        print("> Time to get crafting!")
        time.sleep(2.5)
        letThereBeLine()
        
        while resLeft == True:
            
            # Random rasciiource generation ... change to larger range later
            resType = random.randint(0,7)

            # Tree condition
            if resType == 0 or resType == 1 or resType == 2:
                print("> You can see a tree nearby")
                gatherAble = ["WOOD","WOOD","WOOD"]
                reqTool = "AXE"
                interfaceLaunch(gatherAble,reqTool,resInv,resType,toolInv,craftedInv)
                checkForRes(resCount)

            # Shrub condition
            elif resType == 3 or resType == 4:
                print("> There is a shrub nearby")
                gatherAble = ["LEAVES","STICK","STICK"]
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,resType,toolInv,craftedInv)
                checkForRes(resCount)

            # Rock condition
            elif resType == 5 or resType == 6:
                print("> There is a stonepile near your feet")
                gatherAble = []
                # Randomizes rock count
                for i in range(0,random.randint(1,3)):
                    gatherAble.append("ROCK")
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,resType,toolInv,craftedInv)
                checkForRes(resCount)

            # Vine condition
            elif resType == 7:
                print("> You encounter a vine dangling nearby")
                reqTool = "HANDS"
                gatherAble = ["VINE"]
                interfaceLaunch(gatherAble,reqTool,resInv,resType,toolInv,craftedInv)
                checkForRes(resCount)
                
        endGame()

# ACTUAL PROGRAM START                       

print("\n\nWelcome to")
print("\n<>============================================================<>")
print("   ________  ___   __________  __  ______   _________________  ")
print("  / ___/ _ \/ _ | / __/_  __/ /  |/  / _ | / __/_  __/ __/ _ \ ")
print(" / /__/ , _/ __ |/ _/  / /   / /|_/ / __ |_\ \  / / / _// , _/ ")
print(" \___/_/|_/_/ |_/_/   /_/   /_/  /_/_/ |_/___/ /_/ /___/_/|_|  v2.3")
print("\n<>============================================================<>\n")


# Asciing about the tutorial

chooseTut = input("> Would you like to read the tutorial?\n\n[Y] Yes\n[N] No\n\n>> ")

while chooseTut != "Y" and chooseTut != "y" and chooseTut != "N" and chooseTut != "n":
    letThereBeLine()
    chooseTut = input("> Please select...\n\n[Y] Read the tutorial\n[N] Skip it\n\n>> ")
else:
    if chooseTut == "Y" or chooseTut == "y":
        letThereBeLine()
        print("> The goal of the game is simple: make the coolest items you can!")
        print("> The more complex the item, the more points you recieve.")
        print("> The game ends when you are exhaust the resources around you.")
        print("> Make sure to take note of your location, as location determines resources!")
        print("> The rest is up to you! Go make something awesome!")
       

            
            

            
 # including this instruction to allow functions to be called before they are defined
if __name__ == "__main__": main()
