#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

#environment colors
env = ["red", "orange", "yellow", "green", "blue", "purple"]
rounds = 6
score = 0

#counts of wild birds
nR = 0
nO = 0
nY = 0
nG = 0
nB = 0
nP = 0
total_wild = 0
wild_dict = {}

#counts of zoo birds
nZR = 5
nZO = 5
nZY = 5
nZG = 5
nZB = 5
nZP = 5
total_zoo = 30
zoo_dict = {}

opp_color = ""
adj_color = ""

def print_totals():
    print("Your current wild bird population:")
    print("Red: " + str(wild_dict["red"]))
    print("Orange: " + str(wild_dict["orange"]))
    print("Yellow: " + str(wild_dict["yellow"]))
    print("Green: " + str(wild_dict["green"]))
    print("Blue: " + str(wild_dict["blue"]))
    print("Purple: " + str(wild_dict["purple"]) + "\n")
    total_zoo = sum(zoo_dict.values())
    total_wild = sum(wild_dict.values())
    total = total_zoo + total_wild
    print("Zoo: " + str(total_zoo))
    print("Wild: " + str(total_wild))
    print("Overall total: " +str(total) + "\n")

def color_match(current_env):
    global opp_color
    global adj_color
    if (current_env == "red"):
        opp_color = "green"
        adj_color = ["purple", "orange"]
    elif (current_env == "orange"):
        opp_color = "blue"
        adj_color = ["red", "yellow"]
    elif (current_env == "yellow"):
        opp_color = "purple"
        adj_color = ["orange", "green"]
    elif (current_env == "green"):
        opp_color = "red"
        adj_color = ["yellow", "blue"]
    elif (current_env == "blue"):
        opp_color = "orange"
        adj_color = ["green", "purple"]
    elif (current_env == "purple"):
        opp_color = "yellow"
        adj_color = ["blue", "red"]
    else:
        print("fail")
    return(opp_color, adj_color)

def predation(wild_dict, opp_color):
    animal = ["hawk", "snake", "badger", "fox"]
    predator = random.choice(animal)
    print("\n" + "A " + str(predator) + " attacks!")
    if opp_color in wild_dict:
        wild_dict[opp_color] = 0
        print("\n" + "Your " + str(opp_color) + " birds were very visible in the " + str(current_env) + " habitat and were all eaten.")
    return(wild_dict)    

def reproduce(current_env, wild_dict, adj_color):
    if current_env in wild_dict:
        wild_dict[current_env] += 3
        print("You get +3 for your " + str(current_env) + " birds because they camouflage perfectly."+ "\n")
    for i in adj_color:
        if i in wild_dict:
            wild_dict[i] += 1
            print("You get +1 for your " + str(adj_color) + " birds because they blend in pretty well." + "\n")
    return wild_dict
        
        
def mutation(wild_dict):
    loser_choice = []
    winner_choice = ["red", "orange", "yellow", "green", "blue", "purple"]
    for key, value in wild_dict.items():
        if value != 0:
            loser_choice.append(key)
    loser = random.choice(loser_choice)
    wild_dict[loser] -= 1
    winner = random.choice(winner_choice)
    wild_dict[winner] += 1
    print("\n" + "One " + str(loser) + " bird mutated into a " + str(winner) + " bird." + "\n")
    return wild_dict

def drift(wild_dict):
    t = 0
    option = ["A", "A", "B", "B", "C", "C", "D", "E"]
    loss = random.choice(option)
    if (loss == "A"): 
        text = ["A poacher attacks! Lose 1 bird.", "Your birds get the flu. Lose 1 bird."]
        A = random.choice(text)
        print(str(A))
        loser_choice = []
        for key, value in wild_dict.items():
            if value != 0:
                loser_choice.append(key)
        loser = random.choice(loser_choice)
        wild_dict[loser] -= 1
        print("You lost one " + str(loser) + " bird.")
    elif (loss == "B"):
        text = ["A harsh winter takes it's toll. Lose 2 birds.", "A drought limits food supply. Lose 2 birds."]
        B = random.choice(text)
        print(str(B))
        while t < 2:
            loser_choice = []
            for key, value in wild_dict.items():
                if value != 0:
                    loser_choice.append(key)
            loser = random.choice(loser_choice)
            wild_dict[loser] -= 1
            print("You lost one " + str(loser) + " bird.")
            t += 1
    elif (loss == "C"):
        total = round((sum(wild_dict.values())/2))
        print("A fire destroys nesting locations. Half your birds die.")
        while t < total:
            loser_choice = []
            for key, value in wild_dict.items():
                if value != 0:
                    loser_choice.append(key)
            loser = random.choice(loser_choice)
            wild_dict[loser] -= 1
            print(str(loser) + " lost one bird.")
            t += 1
    else:
        print("\n" + "All your birds are safe!")    
    total_wild = sum(wild_dict.values())
    print ("\n" + "You still have " + str(total_wild) + " wild birds" + "\n")    
    return wild_dict
    
def migrate(wild_dict, zoo_dict): 
    if zoo_dict["ZR"] > 0:
        print("\n" + "Red in zoo: " + str(zoo_dict["ZR"]))
        nR = int(input("Migrate how many red? "))
        while (nZR - nR) < 0:
            nR = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZR) + ": "))
        wild_dict["red"] += nR
        zoo_dict["ZR"] = zoo_dict["ZR"] - nR
    if zoo_dict["ZO"] > 0:  
        print("\n" + "Orange in zoo: " + str(zoo_dict["ZO"]))
        nO = int(input("Migrate how many orange? "))
        while (nZO - nO) <= 0:
            nR = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZO) + ": "))
        wild_dict["orange"] += nO
        zoo_dict["ZO"] = zoo_dict["ZO"] - nO
    if zoo_dict["ZY"] > 0: 
        print("\n" + "Yellow in zoo: " + str(zoo_dict["ZY"]))
        nY = int(input("Migrate how many yellow? "))
        while (nZY - nY) <= 0:
            nY = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZY) + ": "))
        wild_dict["yellow"] += nY
        zoo_dict["ZY"] = zoo_dict["ZY"] - nY
    if zoo_dict["ZG"] > 0: 
        print("\n" + "Green in zoo: " + str(zoo_dict["ZG"]))
        nG = int(input("Migrate how many green? "))
        while (nZG - nG) <= 0:
            nG = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZG) + ": "))
        wild_dict["green"] += nG
        zoo_dict["ZG"] = zoo_dict["ZG"] - nG
    if zoo_dict["ZB"] > 0: 
        print("\n" + "Blue in zoo: " + str(zoo_dict["ZB"]))
        nB = int(input("Migrate how many blue? "))
        while (nZB - nB) <= 0:
            nB = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZB) + ": "))
        wild_dict["blue"] += nB
        zoo_dict["ZB"] = zoo_dict["ZB"] - nB
    if zoo_dict["ZP"] > 0:
        print("\n" + "Purple in zoo: " + str(zoo_dict["ZP"]))
        nP = int(input("Migrate how many purple? "))
        while (nZP - nP) <= 0:
            nP = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZP) + ": "))
        wild_dict["purple"] += nP
        zoo_dict["ZP"] = zoo_dict["ZP"] - nP
    return wild_dict, zoo_dict
##############################################################################

round_no = 1
print("ROUND " + str(round_no) + "\n")
current_env = random.choice(env)
print("Current environment is: " + str(current_env) + "\n" )
print("Each zoo has 5 birds. You can take birds from the zoo and introduce them into the wild." + "\n")
nR = int(input("How many red birds would you like to add from the zoo? " + "\n"))
while (nZR - nR) <= 0:
    nR = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZR) + ": "))
wild_dict["red"] = nR
zoo_dict["ZR"] = nZR - nR
    
nO = int(input("How many orange birds would you like to add from the zoo? " + "\n"))
while (nZO - nO) <= 0:
    nR = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZO) + ": "))
wild_dict["orange"] = nO
zoo_dict["ZO"] = nZO - nO

nY = int(input("How many yellow birds would you like to add from the zoo? " + "\n"))
while (nZY - nY) <= 0:
    nY = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZY) + ": "))
wild_dict["yellow"] = nY
zoo_dict["ZY"] = nZY - nY
    
nG = int(input("How many green birds would you like to add from the zoo? " + "\n"))
while (nZG - nG) <= 0:
    nG = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZG) + ": "))
wild_dict["green"] = nG
zoo_dict["ZG"] = nZG - nG

nB = int(input("How many blue birds would you like to add from the zoo? " + "\n"))
while (nZB - nB) <= 0:
    nB = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZB) + ": "))
wild_dict["blue"] = nB
zoo_dict["ZB"] = nZB - nB

nP = int(input("How many purple birds would you like to add from the zoo? " + "\n"))
while (nZP - nP) <= 0:
    nP = int(input("Invalid. Not enough birds in zoo. Please enter a number equal or less than " + str(nZP) + ": "))
wild_dict["purple"] = nP
zoo_dict["ZP"] = nZP - nP

while (round_no < rounds):
    print("\n" + "---")
    color_match(current_env)
    input("Press enter to encounter predators." + "\n")
    predation(wild_dict, opp_color)
    print("\n" + "---")
    input("Press enter to reproduce." + "\n")
    reproduce(current_env, wild_dict, adj_color)
    print_totals()
    print("\n" + "---")
    input("Press enter to mutate." + "\n")
    mutation(wild_dict)
    print_totals()
    print("\n" + "---")
    input("Press enter to see the effects of drift (chance)." + "\n")
    drift(wild_dict)
    print_totals()
    print("\n" + "---")
    if round_no < (rounds - 1): 
        input("Press enter to migrate." + "\n")
        choice_migrate = input("\n" + "Do you want to add more birds from the zoo? ")
        if (choice_migrate == "y" or "yes") == True:
            migrate(wild_dict, zoo_dict)
            print_totals()
            print("\n" + "---" + "END OF ROUND " + str(round_no)+ "\n")            
        elif (choice_migrate == "n" or "no") == True:
            print_totals()
            print("\n" + "---" + "END OF ROUND " + str(round_no) + "\n")
        input("Press enter for next round." + "\n")            
        print("\n" + "---" + "\n" + "ROUND" + str(round_no + 1) + "\n")
        current_env = random.choice(env)
        print("\n" + "Current environment is: " + str(current_env))
        round_no += 1
    else:
        round_no += 1
print("\n" + "The End!")  
print_totals()
score = (sum(wild_dict.values()) + sum(zoo_dict.values())) - 30
print("You were able to increase your bird population by " + str(score) + " birds.")




