from dataclasses import dataclass

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
@dataclass
class Decomposition:
    age: int
    _type: str
    def run(self):
        # This is an If tree based on each type
        if self._type == "Dpe":
            pass
        elif self._type == "Db":
            pass
        elif self._type == "Dcb":
            pass
        elif self._type == "Dw":
            pass
@dataclass
class SNC:
    age: int
    _type: str
    def run(self,):
        if self._type == "SNCw":
            pass
        elif self._type == "SNCc":
            pass
@dataclass
class Remelting:
    age: int
    _type: str
    def run(self):
        if self._type == "Rm":
            pass
        elif self._type == "Rr":
            pass
        elif self._type == "Rf":
            pass