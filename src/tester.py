# Unit tester for this project
# Makes sure it all works
import json
#testscore = 0

def run():
    #Dictionary Indexing Test
    jsonIDS = open("jsonIDS.json", "r")
    jsoncontents = jsonIDS.read()
    jsonstuff = json.loads(jsoncontents)
    #This is the syntax jsonstuff["DNAs"][0]
    if jsonstuff["DNAextractorIDS"]["Pork"][0]["Failed"] == 60:
        #testscore += 10
        print(jsonstuff["DNAextractorIDS"]["Pork"][0]["Failed"])
    value = list(jsonstuff["DNAextractorIDS"].keys())
    for i in value:
        try:
            abc = jsonstuff["DNAextractorIDS"][i][0]
            bca = jsonstuff["DNAextractorIDS"][i][1]
            print(f"{i} + {bca}")
            Properties = abc.keys()
            for Property in Properties:
                cba = jsonstuff["DNAextractorIDS"][i][0][Property]
                print(f"    {Property}: {cba}%")

        except:
            pass
run()