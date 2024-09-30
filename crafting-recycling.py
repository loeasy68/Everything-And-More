# Codes for everything
#  D - Decomposition - Decomposition(Organics, Plastic) Out(Fertilized Dirt, Oil(Requires plastic))
##  pe - Plastic Eating
##  b - Bacteria
##  cb - Comporter Box
##  w - Worms
#  SNC - Soaking n’ Crush - Soaking n’ Crush(Brick, Glass) Out(Clay, Sand)
##  w - water
##  c - crusher
#  R - Remelting(Metal, Glass) Out(Glass, Ingots)
##  m - molder
##  r - refiner
##  f - furnace
# Example code would look like "Dpe"
class Decomposition:
    def __init__(self, age, _type):
        self.age = age
        self.type = _type
    def run(age, _type):
        # This is an If tree based on each type
        if _type == "Dpe":
            pass
        elif _type == "Db":
            pass
        elif _type == "Dcb":
            pass
        elif _type == "Dw":
            pass
class SNC:
    def __init__(self, age, _type):
        self.age = age
        self.type = _type
    def run(age, _type):
        if _type == "SNCw":
            pass
        elif _type == "SNCc":
            pass
class Remelting:
    def __init__(self, age, _type):
        self.age = age
        self.type = _type
    def run(age, _type):
        if _type == "Rm":
            pass
        elif _type == "Rr":
            pass
        elif _type == "Rf":
            pass