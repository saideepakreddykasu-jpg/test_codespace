Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> units = 100
... material_per_unit = 50
... wastage_percent = 5
... labour_total = 2000
... machine_total = 1500
... selling_price_per_unit = 100
... target_profit = 3000
... 
... material_cost = units * material_per_unit
... wastage_cost = material_cost * wastage_percent / 100
... total_cost = material_cost + wastage_cost + labour_total + machine_total
... revenue = units * selling_price_per_unit
... profit = revenue - total_cost
... 
... print(f"Material cost: Rs.{material_cost:.2f}")
... print(f"Wastage cost: Rs.{wastage_cost:.2f}")
... print(f"Total production cost: Rs.{total_cost:.2f}")
... print(f"Sales revenue: Rs.{revenue:.2f}")
... print(f"Profit: Rs.{profit:.2f}")
