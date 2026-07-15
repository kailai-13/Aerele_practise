from enum import Enum
from dataclasses import dataclass

class Status(Enum):
    """Used store repeated values or strings in more clear and efficient way"""
    PAID="Paid"
    DRAFT="Draft"
    CANCELLED="Cancelled"

@dataclass
class Invoice:
    """Data class that stores information easily accessible"""
    id:str
    customer_name:str
    amount:float
    tax:float
    status:str

class Validate:
    """Validating the given invoice object if it have all the required fields"""
    def __init__(self,invoice):
        self.invoice=invoice
    def validation(self):
        if not self.invoice.customer_name:
            raise ValueError("Customer name is missing!")
        if self.invoice.amount<0:
            raise ValueError("Amount can't be less than 0!")
        if self.invoice.tax<9:
            raise ValueError("Tax can't be less than 0!")
        if not self.invoice.status:
            raise ValueError("Status can't be empty!")
        return "Validation Successfull"
    
#Example showcase is below

invoice1=Invoice("IN01","KAILAI",1200.22,100,Status.PAID)
print(invoice1)

v=Validate(invoice1)
print(v.validation())

invoice2=Invoice("","",11,22,Status.DRAFT)
print(invoice2)

v2=Validate(invoice2)
print(v2.validation())