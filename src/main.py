#Stores IDs instead of abbreviations
#0 - Decompistition/Recycling
#1 - Storage
#2 - Machines
#3 - GMO
#4 Other QOL things
IDtable = [["plastic eating bacteria", "worms", "Remolder", "Soaker", "Refiner", "Smelter"], ["Compacted chest", "Automatic Sorter", "Giga Chest", "Chest networker"], ["Conveyor", "Cobblestone Generator", "Mixer", "Solar panels", "Electric furnace", "Research station"], ["Syringe", ["Insert 50 genes"], "Dna extractor", "Gene Combiner", "Gene Synthesizer"], ["Molten Iron", "Molten Gold", "Molten Stone", "Molten Mix", "Molten Glass"]]
#fyi chest networker should find all the nearby chests by the owner of the chest networker and create a network where they can find all the contents of the chests
class mod:
    def __init__(self) -> None:
        self.name = "everything-and-more"
        self.authors = ["Bob", "Loeasy"]
        self.version = "1.21"
        self.java = "21"
    class storage():
        #Insert chests
        def __init__(self, SS, SC):
            self.storagesize = SS
            self.contents = SC
    class decomposition():
        def __init__(self, age, type):
            self.age = age
            self.type = type
    class machines():
        def __init__(self, MS, MI):
            self.machinestorage = MS
            self.machineinfo = MI
    class QOL():
        def placeholder():
            print("placeholder")
            
        #Insert Decompisition
