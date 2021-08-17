import random

print("Welcome to the Dice program!")
print("You have to create your dice so you can roll it")
proceed = input("Do you want to proceed? y/n")
if(proceed.upper()=='Y'):
    sides = int(input("How many sides do you want your dice to have?"))
    if(sides>0):
        percentages = input("Do you want dice values to represent percentages? y/n")
        evenly = False
        if(percentages.upper()=='Y'):
            evenly = input("Do you want the values to be evenly distributed parts of 100%?")
            if(evenly.upper()=='Y'):
                print()
        while True:
            roll = input("Do you want to roll the dice now? y/n ")
            if roll.upper() == 'Y':
                if(percentages.upper()!='Y'):
                    value = random.randint(1, sides)
                if(percentages.upper()=='Y'):
                    if(evenly.upper()=='Y'):
                        minimal = 100/sides
                        value = round(random.randint(1, sides) * minimal)
                    if(evenly.upper()!='Y'):
                        value = random.randint(10, sides*10)
                print(value)
            else:
                wannaExit = input("Do you really want to quit? y/n ")
                if(wannaExit.upper()=='Y'):
                    exit()
    else:
        print("[Error] You have to provide values that are higher than 0")