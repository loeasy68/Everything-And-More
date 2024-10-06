"""
    This is the storage handler for compact chests, sorters, and storage controllers
"""
chestSize = 5
table2 = []
i = -1
# Working test for table, Other method is in Snippets/tableTest.py
while True:
    i += 1
    if len(table2) > chestSize - 1:
        print("CHEST FILLED")
        break
    else:
        table2.append(["minecraft:iron_ingots", i])
print(table2)

def compactChests():
    pass

def sorters():
    pass

def storageController():
    pass