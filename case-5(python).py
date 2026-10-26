Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
usage_data_gb = 12
usage_minutes = 350
required_validity = 28
budget = 500

... plans = [
...     {"name": "Basic", "price": 199, "data": 5, "minutes": 200,
...      "validity": 28, "extra_data_rate": 30, "extra_minute_rate": 0.50},
...     {"name": "Smart", "price": 399, "data": 15, "minutes": 500,
...      "validity": 56, "extra_data_rate": 25, "extra_minute_rate": 0.40},
...     {"name": "Value", "price": 299, "data": 10, "minutes": 400,
...      "validity": 28, "extra_data_rate": 20, "extra_minute_rate": 0.60},
... ]
... 
... eligible = []
... for plan in plans:
...     if plan["validity"] < required_validity:
...         continue
... 
...     extra_data = max(0, usage_data_gb - plan["data"])
...     extra_minutes = max(0, usage_minutes - plan["minutes"])
...     cost = (plan["price"] + extra_data * plan["extra_data_rate"]
...             + extra_minutes * plan["extra_minute_rate"])
... 
...     if cost <= budget:
...         eligible.append((cost, plan["name"]))
... 
... if eligible:
...     cost, name = min(eligible)
...     print(f"Most economical eligible plan: {name}")
...     print(f"Total cost: Rs.{cost:.2f}")
... else:
