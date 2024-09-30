import json
IDtable = [["plastic eating bacteria", "worms", "Remolder", "Soaker", "Refiner", "Smelter"], 
    ["Compacted chest", "Automatic Sorter", "Giga Chest", "Chest networker"], 
    ["Conveyor", "Cobblestone Generator", "Mixer", "Solar panels", "Electric furnace", "Research station"], 
    ["Dna extractor", "Gene Combiner", "Gene Synthesizer"], 
    ["Molten Iron", "Molten Gold", "Molten Stone", "Molten Mix", "Molten Glass"]
]
GeneCombinerID = [
    ["THE EATER", ["Omnivore", "Fatness/Bulk"]],
    ["Thick Skinned", ["Bulk", "Fatness"]],
    ["Weak Speedster", ["Glass Canon", "Hollow Bones"]],
    ["Buff Speedster", ["Thick Skinned", "Weak Speedster"]],
    ["Le chonk", ["THE EATER", "Thick Skinned"]],
    ["Slow Speedster", ["Le chonk", "Buff Speedster"]]
]
GeneExtractorID = [
    
]
jsonIDS = open("jsonIDS.json", "r")
jsoncontents = jsonIDS.read()
jsonstuff = json.loads(jsoncontents)
#This is the syntax jsonstuff["DNAs"][0]
print(jsonstuff["DNAs"][18])