Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> consultation = 500
... diagnostics = 1200
... treatment = 5000
... concession_rate = 0.10
... qualifies_for_concession = True
... amount_paid = 5000
... 
... subtotal = consultation + diagnostics + treatment
... concession = subtotal * concession_rate if qualifies_for_concession else 0
... total = subtotal - concession
... balance = total - amount_paid
... 
... if amount_paid < 0:
...     status = "Invalid payment"
... elif balance <= 0:
...     status = "Paid"
... elif amount_paid == 0:
...     status = "Unpaid"
... else:
...     status = "Partially paid"
... 
... print(f"Subtotal: Rs.{subtotal:.2f}")
... print(f"Concession: Rs.{concession:.2f}")
... print(f"Total bill: Rs.{total:.2f}")
... print(f"Paid: Rs.{amount_paid:.2f}")
... print(f"Balance: Rs.{max(0, balance):.2f}")
