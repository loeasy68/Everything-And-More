import json
jsonIDS = open("jsonIDS.json", "r")
jsoncontents = jsonIDS.read()
jsonstuff = json.loads(jsoncontents)
#This is the syntax jsonstuff["DNAs"][0]
print(jsonstuff["DNAs"][18])