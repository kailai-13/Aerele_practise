from .database import save_invoice
def calculate_tax(amount):
    return amount*0.10
def validate(invoice):
    if not invoice.id:
        raise ValueError("Must give invoice id!")
    if not invoice.name:
        raise ValueError("Must give customer name!")
    if invoice.amount<0:
        raise ValueError("Amount can't be negative!")
    return "Valid"
def process_invoice(invoice):
    validate(invoice)
    tax=calculate_tax(invoice.amount)
    save_invoice(invoice)
    print(f"Invoice completed with Tax: {tax}")