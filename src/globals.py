import json

jsonIDS = open("jsonIDS.json", "r")
jsoncontents = jsonIDS.read()
jsonstuff = json.loads(jsoncontents)
#This is the syntax jsonstuff["DNAs"][0]
geneExtractorIDs = jsonstuff["DNAextractorIDS"]
DNAs = jsonstuff["DNAs"]
IDTable = jsonstuff["IDtable"]
geneExtractorIDs = jsonstuff["GeneCombinerIDs"]
SideEffects = jsonstuff["SideEffects"]
GeneSynthesizerIDs = jsonstuff["GeneSynthesizerIDs"]