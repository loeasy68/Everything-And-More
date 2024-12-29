#IDs for faster finding
from globals import *
from time import sleep
import random
#fyi chest networker should find all the nearby chests by the owner of the chest networker and create a network where they can find all the contents of the chests
frames = 0
NewID = 0
PLANTS = ["Dandelion", "Potato"]
values = []
stageNumber = []
availableIDs = []
#exec(f"Current = Stage{ID}")
#USE Line .split to find type and value
def storage():
    pass
def StageHandler(type):
    return 0
def decomposition():
    #exec(f"{x}Stage = 0")
    
    for i in PLANTS:
        global NewID
        global values
        global stageNumber
        global availableIDs
        if len(availableIDs) < 1:
            NewID += 1
            value = f"{i}Stage{NewID} = {StageHandler(i)}"
            stageNumber.append(NewID)
            #print(value)
            exec(value) # THIS IS EXECUTING IT
            values.append(f"{i}Stage{NewID}")
        else:
            value = f"{i}Stage{availableIDs[0]} = {StageHandler(i)}"
def machines():
    pass
def QOL():
    pass
def findStageNumber():
    try:
        #x = values[500].split() # [400 Index] is 10.00 sec + Python runtime
        x = random.choice(values)
        print(values)
        print(x)
    except IndexError:
        print("test")
while True:
    decomposition()
    findStageNumber()
    sleep(0.1) #NOTE: Goes twice as fast   
    frames += 1 # NOTE: ALWAYS NEED TO BE AT THE END
