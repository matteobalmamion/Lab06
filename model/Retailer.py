from dataclasses import dataclass
@dataclass
class Retailer:
    code:int
    name:str
    type:str
    country:str

    def __str__(self):
        return f"{self.name}: {self.code}"
    def __eq__(self, other):
        return self.code == other.code
    def __hash__(self):
        return hash(self.code)