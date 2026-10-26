Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> budget_inr = 100000
... conversion_fee_rate = 0.02
... 
... expenses = [
...     {"category": "Hotel", "amount": 300, "currency": "USD", "rate": 83.0},
...     {"category": "Food", "amount": 100, "currency": "EUR", "rate": 90.0},
...     {"category": "Transport", "amount": 150, "currency": "USD", "rate": 83.0},
... ]
... 
... converted = []
... for expense in expenses:
...     inr = expense["amount"] * expense["rate"]
...     fee = inr * conversion_fee_rate
...     total = inr + fee
...     converted.append((expense["category"], total))
...     print(f"{expense['category']}: Rs.{total:.2f}")
... 
... total_spending = sum(amount for _, amount in converted)
... largest = max(converted, key=lambda item: item[1])
... 
... print(f"Total spending: Rs.{total_spending:.2f}")
... print(f"Budget: Rs.{budget_inr:.2f}")
... print("Within budget" if total_spending <= budget_inr else "Over budget")
