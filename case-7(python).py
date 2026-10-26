Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
items = [
...     {"name": "Shirt", "category": "clothing", "price": 1000, "quantity": 2},
...     {"name": "Book", "category": "books", "price": 500, "quantity": 1},
... ]
... 
... tax_rates = {"clothing": 0.05, "books": 0.02}
... discount_threshold = 2000
... discount_rate = 0.10
... max_discount = 300
... 
... subtotal = 0
... tax_total = 0
... 
... print("ITEMIZED INVOICE")
... for item in items:
...     amount = item["price"] * item["quantity"]
...     tax = amount * tax_rates[item["category"]]
...     subtotal += amount
...     tax_total += tax
...     print(f"{item['name']}: Rs.{amount:.2f}, tax Rs.{tax:.2f}")
... 
... discount = min(subtotal * discount_rate, max_discount) if subtotal >= discount_threshold else 0
... total = subtotal + tax_total - discount
... 
... print(f"Subtotal: Rs.{subtotal:.2f}")
... print(f"Tax: Rs.{tax_total:.2f}")
... print(f"Discount: Rs.{discount:.2f}")
