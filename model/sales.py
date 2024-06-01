from dataclasses import dataclass
from datetime import datetime
@dataclass
class Sales:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __str__(self):
        return self.Retailer_code - self.Product_number

    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code and self.Product_number == other.Product_number

    def __hash__(self):
        return hash(self.Retailer_code) ^ hash(self.Product_number)
