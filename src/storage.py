"""
    This is the storage handler for compact chests, sorters, and storage controllers
"""
table1 = [
    [["minecraft:iron", 64], [], []],
    [[], [], []],
    [[], [], []],
    [[], [], []]
    
]

table2 = []
for i in range(60):
    if len(table2) > 12:
        print("CHEST FILLED")
    else:
        table2.append(["minecraft:iron_ingots", i])
print(table2)

#18
try:
    table1[0][0].append("a")
    table1[0][1].append("a")
    table1[0][2].append("a")
    table1[1][0].append("a")
    table1[1][1].append("a")
    table1[1][2].append("a")
    table1[2][0].append("a")
    table1[2][1].append("a")
    table1[2][2].append("a")
    table1[3][0].append("a")
    table1[3][1].append("a")
    table1[3][2].append("a")
    table1[4][0].append("a")
    table1[4][1].append("a")
    table1[4][2].append("a")
    table1[5][0].append("a")
    table1[5][1].append("a")
    table1[5][2].append("a")
except IndexError:
    print("CHEST FILLED")

print(table2)

def compactChests():
    pass

def sorters():
    pass

def storageController():
    pass