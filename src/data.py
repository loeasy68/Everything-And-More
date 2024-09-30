from dataclasses import dataclass

@dataclass
class Storage:
    """Class for keeping track of an item in inventory."""
    StorageContents: list
    def GetContent(self, ID: int) -> float:
        return self.StorageContents[ID]