slabs = [(100, 1.5), (100, 2.5), (float("inf"), 4.0)]
fixed_charge = 50
surcharge_rate = 0.05
rebate = 20

def calculate_bill(units):
    remaining = units
    energy_charge = 0

    for slab_units, rate in slabs:
        used = min(remaining, slab_units)
        energy_charge += used * rate
        remaining -= used
        if remaining <= 0:
            break

    surcharge = energy_charge * surcharge_rate
    total = max(0, energy_charge + fixed_charge + surcharge - rebate)
    return total

monthly_units = {"January": 120, "February": 150, "March": 250}
bills = {}

for month, units in monthly_units.items():
    bills[month] = calculate_bill(units)
    print(f"{month}: {units} units, bill = Rs.{bills[month]:.2f}")

months = list(bills)
print("Unusual increases (>25%):")
for i in range(1, len(months)):
    previous = bills[months[i - 1]]
    current = bills[months[i]]
    increase = (current - previous) / previous * 100
    if increase > 25:
        print(f"{months[i]}: {increase:.1f}% increase")
