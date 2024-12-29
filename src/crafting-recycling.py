from dataclasses import dataclass

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
    def run(self):
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