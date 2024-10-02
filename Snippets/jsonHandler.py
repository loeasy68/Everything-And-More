import json
jsonIDS = open(".././src/jsonIDS.json", "r")
jsoncontents = jsonIDS.read()
jsonstuff = json.loads(jsoncontents)
#This is the syntax jsonstuff["DNAs"][0]
#print(jsonstuff["DNAs"][18])
#Prints all side effects
for i in jsonstuff["SideEffects"]:
    print(i)
