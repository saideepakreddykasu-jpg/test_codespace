Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
passengers = [
...     {"name": "Ravi", "age": 30},
...     {"name": "Meena", "age": 68},
... ]
... distance_km = 500
... travel_class = "Sleeper"
... cancelled = False
... 
... rate_per_km = {"Sleeper": 1.2, "AC": 2.5}
... reservation_fee = {"Sleeper": 20, "AC": 50}
... senior_age = 60
... senior_discount = 0.40
... cancellation_penalty = 100
... 
... rate = rate_per_km[travel_class]
... fee = reservation_fee[travel_class]
... 
... for passenger in passengers:
...     base_fare = distance_km * rate
...     discount = base_fare * senior_discount if passenger["age"] >= senior_age else 0
...     fare = base_fare - discount + fee
... 
...     refund = max(0, fare - cancellation_penalty) if cancelled else 0
...     print(f"{passenger['name']}: Fare Rs.{fare:.2f}", end="")
...     if cancelled:
...         print(f", Refund Rs.{refund:.2f}")
...     else:
