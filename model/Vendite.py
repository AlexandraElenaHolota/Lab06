from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vendite:
    Date: datetime
    Retailer_code: int
    Product_number: int
    Ricavo: float

    def __str__(self):
        return f"Data: {self.Date}; Ricavo { self.Ricavo}, Retailer { self.Retailer_code}, Product { self.Product_number}"

    def __hash__(self):
        return hash(self.Date) ^ hash(self.Retailer_code) ^ hash(self.Product_number)

    def __eq__(self, other):
        return self.Ricavo!=other.Ricavo

    def __lt__(self, other):
        return self.Ricavo<other.Ricavo