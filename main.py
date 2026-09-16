from pyscript import display
from js import document

def create_order(e):
    document.getElementbyId('order').HTML = ""

    drink1 = document.getElementbyId('drink1')
    drink2 = document.getElementbyId('drink2')
    drink3 = document.getElementbyId('drink3')
    drink4 = document.getElementbyId('drink4')
    drink5 = document.getElementbyId('drink5')


    subtotal = float(drink1.value) * drink1.checked + float(drink2.value) * drink2.checked + float(drink3.value) * drink3.checked + float(drink4.value) * drink4.checked + float(drink5.value) * drink5.checked

    vat = subtotal * 0.12
    amount_due = subtotal + vat

    display(
        "Dani's Boba Shop!",
        f"Subtotal: ₱{subtotal:.2f}",
        f"VAT: ₱{vat:.2f}",
        f"Amount Due: ₱{amount_due.2f}",
        target="reciept"
    )
