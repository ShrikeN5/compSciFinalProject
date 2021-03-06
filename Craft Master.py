#!usr/bin/python3
# Program Name: CRAFT MASTER
# Program Description: Material gathering and crafting game
#  by MAARTEN BERGSMA, KEEGAN KIRKWOOD, AND LUKE BEUHLER    www.bergsmaarten@gmail.com
# Python 3.5.0 program template in Guerin computer science course
# Dec 2015, Vers 5.1

import random
import time

resInv = []
craftedInv = []
toolInv = ["HANDS"]
resLeft = True
resCount = 10
knownKeys = []
knownValues = []

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
        print("> You can gather",resCount,"more resources")
    return

def letThereBeLine():
    print("\n<>==================================================<>\n")
    return

def letThereBeCloseLine():
    print("\n<>==================================================<>")
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

def craftBook():
    global knownKeys
    global knownValues

    letThereBeCloseLine()
    print("   ___  ________________  ________")
    print("  / _ \/ __/ ___/  _/ _ \/ __/ __/")
    print(" / , _/ _// /___/ // ___/ _/_\ \  ")
    print("/_/|_/___/\___/___/_/  /___/___/  ")
    letThereBeLine()

    print("> In order to craft, choose the items you want to use in the select menu")
    print("> Once you have chosen the items press 'Q' to go back to the crafting interface")
    print("> Selece 'CRAFT' and your item will be crafted")
    print("> Once you have crafted an item, its recipe will stay written in your recipe book.")
    
    letThereBeLine()

    if len(knownKeys) <= 0:
        print("> You don't know any recipes yet...")
    else:
        print("> These are the recipes you already know:\n")
        for i in range(0,len(knownKeys)):
            print(knownKeys[i],":",",".join(knownValues[i]))
            

# Launches the player interface
def interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID):
    global resCount
    while len(gatherAble) > 0:

        # Resource type message generator
        if textID == 0:
            print("> There is a",resText,"nearby")
        elif textID == 1:
            print("> You can see a",resText,"from here")
        elif textID == 2:
            print("> You encounter a",resText)
        elif textID == 3:
            print("> You run into a",resText)
        elif textID == 4:
            print("> The",resText,"is still there")
        elif textID == 5:
            print("> There is nothing left to gather from the",resText)

        letThereBeLine()

        # Interface logic
        playerAction = input("  [1] CRAFT   [2] GATHER   [3] INVENTORY   [4] MOVE\n\n>> ")
        while playerAction != "1" and playerAction != "2" and playerAction != "3" and playerAction != "4":
            letThereBeLine()
            playerAction = input("> Please select...\n\n  [1] CRAFT   [2] GATHER   [3] INVENTORY   [4] MOVE\n\n>> ")

        # Craft condition - required craftEngine() function
        if playerAction == "1":
            craftEngine(resInv,toolInv,craftedInv)

        # Gather condition
        elif playerAction == "2":
            letThereBeCloseLine()
            print("  ________ ________ _________ ")
            print(" / ___/ _ /_  __/ // / __/ _ \ ")
            print("/ (_ / __ |/ / / _  / _// , _/")
            print("\___/_/ |_/_/ /_//_/___/_/|_| ")
            letThereBeLine()
            if "NOTHING" in gatherAble:
                textID = 5
                gatherAble.append("NOTHING")
                break
            if reqTool in toolInv:
                print("> Collected",gatherAble[0],"with",reqTool)
                print(">",gatherAble[0],"added to inventory")
                resInv.append(gatherAble.pop(0))
                resCount -= 1
                if len(gatherAble) <= 0:
                    gatherAble.append("NOTHING")
                    textID = 5
                else:
                    textID = 4
            else:
                print("> You cannot collect",gatherAble[0])
                print("> You need to craft a(n)",reqTool,"before you can collect this resource")
                textID = 4

        # Inventory conditon
        elif playerAction == "3":
             inventoryLaunch(resInv, toolInv, craftedInv)
             if "NOTHING" in gatherAble:
                textID = 5
             else:
                textID = 4

        # Move condition
        elif playerAction == "4":
            
            letThereBeCloseLine()
            print("   __  _______ _   ______")
            print("  /  |/  / __ \ | / / __/")
            print(" / /|_/ / /_/ / |/ / _/  ")
            print("/_/  /_/\____/|___/___/  ")
            letThereBeLine()
            
            return
    
    interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
    return

def craftEngine(resInv,toolInv,craftedInv):
    global knownKeys
    global knownValues
    global score
    selectedItems = []
    doneCraft = False
    while doneCraft == False:
        
        letThereBeCloseLine()
        print("  ________  ___   __________")
        print(" / ___/ _ \/ _ | / __/_  __/")
        print("/ /__/ , _/ __ |/ _/  / /   ")
        print("\___/_/|_/_/ |_/_/   /_/    ")
        letThereBeLine()
        
        craftAction = input("  [1] SELECT   [2] CRAFT   [3] INVENTORY   [4] DONE\n\n>> ")
        while craftAction != "1" and craftAction != "2" and craftAction != "3" and craftAction != "4":
            letThereBeLine()
            craftAction = input("> Please select...\n\n  [1] SELECT   [2] CRAFT   [3] INVENTORY   [4] DONE\n\n>> ")

        # Selection system
        if craftAction == "1":
            doneSelect = False

            while doneSelect == False:
                x = []   # List that is checked for matches during item selection, not crafting
                for i in range(1,len(resInv)+1):
                    x.append(str(i))
                    
                letThereBeLine()
                
                if len(resInv) <= 0:
                    print("> You have selected [","-".join(selectedItems),"]") 
                    print("> You can't select any more resources")
                    break
                    
                print("> Select the items you want to craft:\n")
                for i in range(1,len(resInv)+1):
                      print(i,resInv[i-1])
                print("\n> You have selected [","-".join(selectedItems),"]")
                letThereBeLine()
                itemSelect = input("  [R] RECIPES   [C] CLEAR   [X] DELETE   [Q] BACK\n\n>> ")
                
                while itemSelect not in x and itemSelect != "C" and itemSelect != "c" \
                      and itemSelect != "R" and itemSelect != "X" and itemSelect != "x"\
                      and itemSelect != "Q" and itemSelect != "q" and itemSelect != "r":
            
                    itemSelect = input("\n> Please make a selection\n\n>> ")

                for i in range(1,len(resInv)+1):
                    if itemSelect == str(i):
                        selectedItems.append(resInv.pop(i-1))

                    # Go back to craft interface
                    elif itemSelect == "Q" or itemSelect == "q":
                        doneSelect = True
                        break;break

                    # Clear list of selected items
                    elif itemSelect == "C" or itemSelect == "c":
                        for i in range(0,len(selectedItems)):
                            resInv.append(selectedItems.pop())
                        break
                      
                    # Delete items in selected list
                    elif itemSelect == "X" or itemSelect == "x":
                        selectedItems = []
                        break

                    # Help with recipes and crafting
                    elif itemSelect == "R" or itemSelect == "r":
                        craftBook()
                        break
                        

        # Check the selected items list against the list of recipes
        if craftAction == "2":
                      
            resKeys = list(resRecipes.keys())
            resValues = list(resRecipes.values())
            toolKeys = list(toolRecipes.keys())
            toolValues = list(toolRecipes.values())


            # Search for match in recipe list
            for i in range(0,len(resRecipes)):
                isMatch = True
                for item in selectedItems:
                    if item not in resValues[i]:
                        isMatch = False
                    else:
                        continue
                for item2 in resValues[i]:
                    if item2 not in selectedItems:
                        isMatch = False
                    else:
                        continue
                if selectedItems == []:
                    isMatch = False

                # If match found in resource recipe list...

                if isMatch == True:
                    letThereBeLine()
                    print("> You have crafted a(n)",resKeys[i])
                    print(">",resKeys[i],"added to CRAFTED inventory")
                    craftedInv.append(resKeys[i])
                    knownKeys.append(resKeys[i])
                    knownValues.append(resValues[i])
                    selectedItems = []

            # Search for match in tool list
            for i in range(0,len(toolRecipes)):
                isMatch = True
                for item1 in selectedItems:
                    if item1 not in toolValues[i]:
                        isMatch = False
                    else:
                        continue
                for item2 in toolValues[i]:
                    if item2 not in selectedItems:
                        isMatch = False
                    else:
                        continue
                if selectedItems == []:
                    isMatch = False

                # If match found in tool recipe list...
                if isMatch == True:
                    letThereBeLine()
                    print("> You have crafted a(n)",toolKeys[i])
                    print(">",toolKeys[i],"added to TOOLS inventory")
                    toolInv.append(toolKeys[i])
                    knownKeys.append(toolKeys[i])
                    knownValues.append(toolValues[i])
                    selectedItems = []
                      
            if selectedItems != []:
                letThereBeLine()
                print("Craft failed")
                
        # Internal crafting inventory condition
        if craftAction == "3":
            inventoryLaunch(resInv, toolInv, craftedInv)

        # Craft go back condition
        if craftAction == "4":
            for i in range(0,len(selectedItems)):
                resInv.append(selectedItems.pop())
            letThereBeLine()
            doneCraft = True
            
    
# Launches the main inventory interface
def inventoryLaunch(resInv, toolInv, craftedInv):
    goBack1 = False
    while goBack1 == False:
        
        letThereBeCloseLine()
        print("   _____  ___   _______  ____________  _____  __ ")
        print("  /  _/ |/ / | / / __/ |/ /_  __/ __ \/ _ \ \/ / ")
        print(" _/ //    /| |/ / _//    / / / / /_/ / , _/\  /  ")
        print("/___/_/|_/ |___/___/_/|_/ /_/  \____/_/|_| /_/   ")                                               
        letThereBeLine()
        
        goBack1 = False
        invInput = input("  [1] RESOURCES   [2] TOOLS   [3] CRAFTED   [4] BACK\n\n>> ")
        while invInput != "1" and invInput != "2" and invInput != "3" and invInput != "4":
            letThereBeLine()
            invInput = input("> Please select...\n\n  [1] RESOURCES   [2] TOOLS   [3] CRAFTED   [4] BACK\n\n>> ")
            
        # Resource inventory condition
        if invInput == "1":
            letThereBeLine()
            print("You have",len(resInv),"resources:")
            for i in resInv:
                print(i)
                
        # Tool inventory condition
        if invInput == "2":
            letThereBeLine()
            print("You have",len(toolInv),"tools:")
            for i in toolInv:
                print(i)
                
        # Crafted inventory condition
        if invInput == "3":
            letThereBeLine()
            print("You have crafted",len(craftedInv),"items:")
            for i in craftedInv:
                print(i)

        # Go back condition
        if invInput == "4":
            letThereBeLine()
            goBack1 = True
    return
        
# Game over interface
def endGame():
    global resInv
    global craftedInv
    global toolinv
    
    print("> You have exhausted the resources around you")
    print("> There is still time to craft the resources you have already gathered...")
    doneCraft = False
    while doneCraft == False:
        craftEngine(resInv,toolInv,craftedInv)
        doneInput = input("> Are you sure you are done crafting?\n\n[Y] Yes\n[N] No\n\n>> ")
        while doneInput != "Y" and doneInput != "y" and doneInput != "n" and doneInput != "N":
            letThereBeLine()
            pickLocation = input("> Please select...\n\n[Y] I am done\n[N] I'm not done yet\n\n>> ")
        if doneInput == "Y" or doneInput == "y":
            letThereBeLine()
            print("You have crafted...\n")
            for i in craftedInv:
                print(">",i)
                time.sleep(0.5)
            print("\n> With the items you have crafted, you were able to survive a total of",\
                  len(craftedInv)+len(toolInv),"days.")
            letThereBeLine()
            print("> Thanks for playing!")
            doneCraft = True
        else:
            continue
    return
        

################################################################################

       
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
        trueLocation = str(random.randint(1,4)) # This has GOT to be a string to work with rest of program
                           
    if pickLocation == "Y" or pickLocation == "y":
        letThereBeLine()
        trueLocation = input("> Where do you want to go?\n\n[1] Forest\n[2] Mountains\n[3] Desert\n[4] Island\n\n>> ")
        while trueLocation != "1" and trueLocation != "2" and trueLocation != "3" and trueLocation != "4":
            letThereBeLine()
            trueLocation = input("> Please select:\n\n[1] Forest\n[2] Mountains\n[3] Desert\n[4] Island\n\n>> ")
            
    giveMeSpace()
                              
    # True location FOREST
    if trueLocation == "1":
        letThereBeCloseLine()
        print("   ________  ___  ______________")
        print("  / __/ __ \/ _ \/ __/ __/_  __/")
        print(" / _// /_/ / , _/ _/_\ \  / /   ")
        print("/_/  \____/_/|_/___/___/ /_/    ")
        letThereBeLine()
        
        # Story introduction for FOREST ... take time comments out later
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
            
            # Random resource generation ... change to larger range later
            resType = random.randint(0,13)
            textID = random.randint(0,3)

            # Tree condition
            if resType == 0 or resType == 1:
                resText = "TREE"
                gatherAble = ["WOOD","WOOD","WOOD"]
                reqTool = "AXE"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Shrub condition
            elif resType == 2 or resType == 3:
                resText = "SHRUB"
                gatherAble = ["LEAVES","STICK","STICK"]
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Stonepile condition
            elif resType == 4 or resType == 5:
                resText = "STONEPILE"
                gatherAble = []
                # Randomizes rock count
                for i in range(0,random.randint(1,2)):
                    gatherAble.append("ROCK")
                # Randomize chance for flint
                flintChance = random.randint(1,2)
                if flintChance == 1:
                    gatherAble.append("FLINT")
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vine condition
            elif resType == 6 or resType == 7:
                resText = "VINE"
                reqTool = "HANDS"
                gatherAble = ["CORD"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Rabbit condition
            elif resType == 8:
                resText = "RABBIT"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Pond condition
            elif resType == 9:
                resText = "POND"
                reqTool = "HANDS"
                gatherAble = ["FRESHWATER"]
                # Randomizes fish spawn chance
                fishChance = random.randint(1,4)
                if fishChance == 1:
                    gatherAble.append("UNLUCKY FISH")
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vegetable condition
            elif resType == 10:
                resText = "SUSPICIOUS ROOT"
                reqTool = "HANDS"
                gatherAble = ["POTATO"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Mine condition
            elif resType == 11:
                resText = "MINERAL VEIN"
                reqTool = "PICKAXE"
                gatherAble = ["ORE","ORE"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # FIRE condition
            elif resType == 11:
                resText = "DRY LEAVES"
                reqTool = "FIRESTARTER"
                gatherAble = ["TORCH"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 12:
                resText = "LAKE"
                reqTool = "FISHING POLE"
                gatherAble = ["UNLUCKY FISH","UNLUCKY FISH"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 12:
                resText = "DEER"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT","MEAT","MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 13:
                resText = "LOT OF NOTHING"
                reqTool = "HANDS"
                gatherAble = ["SALT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            

        endGame()
    # True location Mountain   (ADDED CODE HERE)
    if trueLocation == "2":
        letThereBeCloseLine()
        print("   __  _______  __  ___  ___________   _____  __")
        print("  /  |/  / __ \/ / / / |/ /_  __/ _ | /  _/ |/ /")
        print(" / /|_/ / /_/ / /_/ /    / / / / __ |_/ //    / ")
        print("/_/  /_/\____/\____/_/|_/ /_/ /_/ |_/___/_/|_/  ")
                                               
        letThereBeLine()
        
        # Story introduction for Mountain ... take time comments out later
        time.sleep(1)
        print("> You suddenly wake up on top of a high mountain.")
        time.sleep(2.5)
        print("> You look over the edge...")
        ponderSec()
        print("> There's nobody around ... all you see is a deep ravine.")
        time.sleep(2.5)
        print("> However, there are many natural resources around you.")
        time.sleep(2.5)
        print("> You realize that the only way to survive is to explore and gather.")
        print("> Time to get crafting!")
        time.sleep(2.5)
        
        while resLeft == True:
            
            # Random resource generation ... change to larger range later
            resType = random.randint(0,16)
            textID = random.randint(0,3)

            # Tree condition
            if resType == 0 or resType == 1:
                resText = "PINE TREE"
                gatherAble = ["WOOD","WOOD","WOOD"]
                reqTool = "AXE"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Shrub condition
            elif resType == 2 or resType == 3:
                resText = "SPROUTING PLANT"
                gatherAble = ["LEAVES","STICK","STICK"]
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Stonepile condition
            elif resType == 4 or resType == 5:
                resText = "CRUMBLING BOULDER"
                gatherAble = []
                # Randomizes rock count
                for i in range(0,random.randint(1,2)):
                    gatherAble.append("ROCK")
                # Randomize chance for flint
                flintChance = random.randint(1,1)
                if flintChance == 1:
                    gatherAble.append("FLINT")
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vine condition
            elif resType == 6 or resType == 7:
                resText = "TWISTED ROPE"
                reqTool = "HANDS"
                gatherAble = ["CORD"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Rabbit condition
            elif resType == 8:
                resText = "SWIFT RABBIT"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Pond condition
            elif resType == 9:
                resText = "COLD POND"
                reqTool = "HANDS"
                gatherAble = ["FRESHWATER"]
                # Randomizes fish spawn chance
                fishChance = random.randint(1,4)
                if fishChance == 1:
                    gatherAble.append("UNLUCKY FISH")
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vegetable condition
            elif resType == 10:
                resText = "SUSPICIOUS ROOT"
                reqTool = "HANDS"
                gatherAble = ["POTATO"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 11:
                resText = "MINERAL VEIN"
                reqTool = "PICKAXE"
                gatherAble = ["ORE","ORE"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 12:
                resText = "CAVE BEAR"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT","MEAT","MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 13:
                resText = "BIRDS NEST"
                reqTool = "HANDS"
                gatherAble = ["FEATHER","FEATHER","EGG"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 14:
                resText = "DRY MOSS"
                reqTool = "FIRESTARTER"
                gatherAble = ["TORCH"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 16:
                resText = "LOT OF NOTHING"
                reqTool = "HANDS"
                gatherAble = ["SALT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 17:
                resText = "LOFTY FRUIT TREE"
                reqTool = "GRAPPLING HOOK"
                gatherAble = ["PINEAPPLE","PINEAPPLE"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

        endGame()

        # True location DESERT   (ADDED CODE HERE)
    if trueLocation == "3":
        letThereBeCloseLine()
        print("   ___  _______________  ______")
        print("  / _ \/ __/ __/ __/ _ \/_  __/")
        print(" / // / _/_\ \/ _// , _/ / /   ")
        print("/____/___/___/___/_/|_| /_/    ")
                             
        letThereBeLine()
        
        # Story introduction for Desert ... take time comments out later
        time.sleep(1)
        print("> You suddenly wake up on in the middle of a desert.")
        time.sleep(2.5)
        print("> You look around.")
        ponderSec()
        print("> There's nobody around ... only you... and a pikachu")
        time.sleep(2.5)
        print("> However, there are many natural resources around you.")
        time.sleep(2.5)
        print("> You realize that the only way to survive is to explore and gather.")
        print("> Time to get crafting!")
        time.sleep(2.5)
        letThereBeLine()
        
        while resLeft == True:
            
            # Random resource generation ... change to larger range later
            resType = random.randint(0,16)
            textID = random.randint(0,3)

            # Tree condition
            if resType == 0 or resType == 1:
                resText = "CACTUS"
                gatherAble = ["SPINES","STALK","STALK"]
                reqTool = "AXE"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Shrub condition
            elif resType == 2 or resType == 3:
                resText = "TUMBLE WEED"
                gatherAble = ["LEAVES","STICK","STICK"]
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Stonepile condition
            elif resType == 4 or resType == 5:
                resText = "PEBBLE PILE"
                gatherAble = []
                # Randomizes rock count
                for i in range(0,random.randint(1,2)):
                    gatherAble.append("ROCK")
                # Randomize chance for flint
                flintChance = random.randint(1,2)
                if flintChance == 1:
                    gatherAble.append("FLINT")
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vine condition
            elif resType == 6 or resType == 7:
                resText = "DESERT VINE"
                reqTool = "HANDS"
                gatherAble = ["CORD"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Rabbit condition
            elif resType == 8:
                resText = "JACKRABBIT"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Pond condition
            elif resType == 9:
                resText = "HIDDEN OASIS"
                reqTool = "HANDS"
                gatherAble = ["FRESHWATER"]
                # Randomizes fish spawn chance
                fishChance = random.randint(1,4)
                if fishChance == 1:
                    gatherAble.append("UNLUCKY FISH")
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vegetable condition
            elif resType == 10:
                resText = "TINY SPROUT"
                reqTool = "HANDS"
                gatherAble = ["POTATO"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 11:
                resText = "MINERAL VEIN"
                reqTool = "PICKAXE"
                gatherAble = ["ORE","ORE"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 12:
                resText = "CAMEL"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT","MEAT","MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)
                  
            elif resType == 12 or resType == 13:
                resText = "EMPTY CRATE"
                reqTool = "HANDS"
                gatherAble = ["WOOD","WOOD"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 14:
                resText = "DRY FUR"
                reqTool = "FIRESTARTER"
                gatherAble = ["TORCH"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 15:
                resText = "BIRDS NEST"
                reqTool = "HANDS"
                gatherAble = ["FEATHER","FEATHER","EGG"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 16:
                resText = "LOT OF NOTHING"
                reqTool = "HANDS"
                gatherAble = ["SALT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            
            

        endGame()

        # True location Island   (ADDED CODE HERE)
    if trueLocation == "4":
        letThereBeCloseLine()
        print("   __________   ___   _  _____") 
        print("  /  _/ __/ /  / _ | / |/ / _ \ ")
        print(" _/ /_\ \/ /__/ __ |/    / // /")
        print("/___/___/____/_/ |_/_/|_/____/")
       
               
        letThereBeLine()
        
        # Story introduction for Island ... take time comments out later
        time.sleep(1)
        print("> You suddenly wake up on a lonely island")
        time.sleep(2.5)
        print("> You look around.")
        ponderSec()
        print("> There's nobody around ... only you... and a Zigzagoon")
        time.sleep(2.5)
        print("> You see the ocean and the beach nearby")
        time.sleep(2.5)
        print("> However, there are many natural resources around you.")
        time.sleep(2.5)
        print("> You realize that the only way to survive is to explore and gather.")
        print("> Time to get crafting!")
        time.sleep(2.5)
        letThereBeLine()
        
        while resLeft == True:
            
            # Random resource generation ... change to larger range later
            resType = random.randint(0,16)
            textID = random.randint(0,3)

            # Tree condition
            if resType == 0 or resType == 1:
                resText = "COCONUT TREE"
                gatherAble = ["WOOD","WOOD","COCONUT"]
                reqTool = "AXE"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Shrub condition
            elif resType == 2 or resType == 3:
                resText = "TROPICAL BUSH"
                gatherAble = ["LEAVES","STICK","STICK"]
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Stonepile condition
            elif resType == 4 or resType == 5:
                resText = "CRAG"
                gatherAble = []
                # Randomizes rock count
                for i in range(0,random.randint(1,2)):
                    gatherAble.append("ROCK")
                # Randomize chance for flint
                flintChance = random.randint(1,2)
                if flintChance == 1:
                    gatherAble.append("FLINT")
                reqTool = "HANDS"
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vine condition
            elif resType == 6 or resType == 7:
                resText = "YUCCA PLANT"
                reqTool = "HANDS"
                gatherAble = ["CORD"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Rabbit condition
            elif resType == 8:
                resText = "DERP IGUANA"
                reqTool = "BOW & ARROW"
                gatherAble = ["MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Pond condition
            elif resType == 9:
                resText = "HOT SPRING"
                reqTool = "HANDS"
                gatherAble = ["FRESHWATER"]
                # Randomizes fish spawn chance
                fishChance = random.randint(1,4)
                if fishChance == 1:
                    gatherAble.append("UNLUCKY FISH")
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            # Vegetable condition
            elif resType == 10:
                resText = "SUSPICIOUS ROOT"
                reqTool = "HANDS"
                gatherAble = ["POTATO"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 11:
                resText = "FRUIT TREE"
                reqTool = "HANDS"
                gatherAble = ["PINEAPPLE"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 12:
                resText = "MINERAL VEIN"
                reqTool = "PICKAXE"
                gatherAble = ["ORE","ORE"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 13:
                resText = "DODO BIRD"
                reqTool = "BOW & ARROW"
                gatherAble = ["FEATHER","MEAT","MEAT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 14:
                resText = "BIRDS NEST"
                reqTool = "HANDS"
                gatherAble = ["FEATHER","FEATHER","EGG"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 15:
                resText = "DRY THATCHING"
                reqTool = "FIRESTARTER"
                gatherAble = ["TORCH"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

            elif resType == 16:
                resText = "LOT OF NOTHING"
                reqTool = "HANDS"
                gatherAble = ["SALT"]
                interfaceLaunch(gatherAble,reqTool,resInv,toolInv,craftedInv,resText,textID)
                checkForRes(resCount)

        endGame()

##############################################################################

# Recipe layout: "NAME":["REQIREMENT","REQUIREMENT","ETC.","SCORE BONUS"]
                      
resRecipes = {"FISH & CHIPS":["UNLUCKY FISH","POTATO"],"BANQUET":["MEAT","POTATO","FRESHWATER"],\
              "MEAL":["FRESHWATER","POTATO"],"HEARTY MEAL":["FRESHWATER","MEAT"],\
              "SHELTER":["WOOD","WOOD","WOOD","CORD"],"KNIFE":["FLINT","STICK"],\
              "POTATO ON A STICK":["POTATO","STICK"],"SEARED FISH":["TORCH","UNLUCKY FISH"],\
              "METAL":["ORE","TORCH"],"FLAMETHROWER":["TORCH","ORE","WOOD","CORD"],\
              "PINA COLADA":["PINEAPPLE","COCONUT","FRESHWATER"],"BONFIRE":["WOOD","WOOD","TORCH"],\
              "ARROW":["FEATHER","STICK","FLINT"],"CAMPFIRE":["TORCH","WOOD"],\
              "BREAKFAST":["EGG","MEAT","FRESHWATER"],"FRUIT JUICE":["PINEAPPLE","FRESHWATER"],\
              "JERKY":["SALT","MEAT"]}

toolRecipes = {"AXE":["STICK","CORD","ROCK"],"BOW & ARROW":["STICK","STICK","CORD","FLINT","FEATHER"],\
               "FISHING POLE":["STICK","CORD"],"FIRESTARTER":["STICK","STICK"],"PICKAXE":["ROCK","CORD","STICK","FLINT"],\
               "GRAPPLING HOOK":["CORD","ORE"],"BOW & ARROW":["STICK","STICK","CORD","FLINT","LEAVES"],\
               "BOW & ARROW":["STICK","STICK","CORD","ORE","LEAVES"],"BOW & ARROW":["STICK","STICK","CORD","ORE","FEATHER"]}

##############################################################################

# ACTUAL PROGRAM START                       

print("\n\nWelcome to\n")
print(" ██████╗██████╗  █████╗ ███████╗████████╗            ")
print("██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝            ")
print("██║     ██████╔╝███████║█████╗     ██║               ")
print("██║     ██╔══██╗██╔══██║██╔══╝     ██║               ")
print("╚██████╗██║  ██║██║  ██║██║        ██║               ")
print(" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝               ")
print("                                                     ")
print("███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗  ")
print("████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗ ")
print("██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝ ")
print("██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗ ")
print("██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║ ")
print("╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ v5.1")
letThereBeLine()


# Asciing about the tutorial

chooseTut = input("> Would you like to read the tutorial?\n\n[Y] Yes\n[N] No\n\n>> ")

while chooseTut != "Y" and chooseTut != "y" and chooseTut != "N" and chooseTut != "n":
    letThereBeLine()
    chooseTut = input("> Please select...\n\n[Y] Read the tutorial\n[N] Skip it\n\n>> ")

if chooseTut == "Y" or chooseTut == "y":
    
    letThereBeCloseLine()
    print(" ________  ____________  ___  _______   __ ")
    print("/_  __/ / / /_  __/ __ \/ _ \/  _/ _ | / / ")
    print(" / / / /_/ / / / / /_/ / , _// // __ |/ /__")
    print("/_/  \____/ /_/  \____/_/|_/___/_/ |_/____/")
    letThereBeLine()
    
    print("> The goal of the game is simple create the best items you can to survive!")
    print("> The more complex or practical the item, the more points you recieve")
    print("> The game ends when you are exhaust the resources around you")
    print("> Make sure to take note of your location, as location determines resource types")
    print("> The rest is up to you! Good luck!")
    
letThereBeLine()

diffSet = int(input("> Enter resource gather limit (difficulty):\n\n>> "))
resCount = diffSet

    


 # including this instruction to allow functions to be called before they are defined
if __name__ == "__main__": main()
