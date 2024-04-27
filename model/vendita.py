import datetime
from dataclasses import dataclass
@dataclass
class Vendita:
    retailer:int
    prodotto:int
    data:datetime.datetime
    quantita:int
    valore:int
    prezzo:int
    ricavo:int

    def __str__(self):
        return f"Data: {self.data}; Ricavo: {self.ricavo}; retailer: {self.retailer}; Prodotto: {self.prodotto}"

    def __eq__(self, other):
        return self.retailer==other.retailer and self.prodotto==other.prodotto and self.data==other.data and self.quantita==other.quantita and self.valore==other.valore and self.prezzo==other.prezzo
    def __hash__(self):
        return hash((self.retailer,self.prodotto,self.data,self.quantita,self.valore,self.prezzo))
