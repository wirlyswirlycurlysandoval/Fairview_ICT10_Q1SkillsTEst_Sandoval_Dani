from pyscript import display
from js import document

def create_order(e):
    document.getElementById("order").innerHTML = ""
    drink1 = document.getElementById("drink1")
    drink2 = document.getElementById("drink2")
    drink3 = document.getElementById("drink3")
    drink4 = document.getElementById("drink4")
    drink5 = document.getElementById("drink5")
    large = document.getElementById("large")

    subtotal = float(drink1.value) * drink1.checked + float(drink2.value) * drink2.checked + float(drink3.value) * drink3.checked + float(drink4.value) * drink4.checked + float(drink5.value) * drink5.checked + float(large.value) * large.checked

    vat = subtotal * 0.12
    grand_total = subtotal + vat
    display(f"Subtotal: {subtotal}", f"VAT: {vat}", f"Grand Total: {grand_total}", target="order")