from .services import process_invoice
from .model import Invoice
def get_inputs():
    name=input("Enter your name:")
    amount=int(input("Enter required Amount:"))
    return name,amount
def process():
    name,amount=get_inputs()
    id="in1"
    invoice = Invoice(id,name,amount)
    process_invoice(invoice)
    
if __name__=="__main__":
    process()