'''
Jonathan Thompson
IS 303 - A02

Shipping Calculator
This program calculates shipping cost based on package weight and
destination zone.

Inputs:
- Customer name (string)
- Package weight in pounds (float)
- Destination zone: local, regional, or national (string)

Processes:
- Validate weight (must be positive)
- Validate zone (must be local, regional, or national)
- Determine base rate from weight tier (under 2 lbs, 2-20 lbs, 20-70 lbs, over 70 lbs)
- Apply zone multiplier (local = 1.0, regional = 1.5, national = 2.5)
- Calculate total shipping cost

Outputs:
- Print customer name, weight, zone, and total shipping cost
- Print error message if any input is invalid
'''


# Inputs
name = input("Name: ")
weight = input("Package Weight (lbs): ")
destination = input("Destination (local, regional, or national): ").lower()


# Time Input Validation
valid_weight = False
weight_validation = weight.replace(".","",1)
weight_is_int = weight_validation.isdigit()

if weight_is_int == True:
    weight = float(weight)
    if weight > 0 and weight <= 70:
        valid_weight = True
    elif weight > 70 and weight <= 150:
        valid_weight = True
        print("Caution: Overweight items are subject to additional shipping fees.")
else:
    print("Invalid weight. Please enter a number between 0 and 150.")


# Destination Input Validation
valid_destination = False
if destination == "local" or destination == "regional" or destination =="national":
    valid_destination = True
else:
    print("Invalid destination. Please enter Local, Regional, or National.")


# Caluclate Shipping cost based off of inputs
if valid_weight == True and valid_destination == True:
    
    base_rate = 1
    if weight < 2:
        base_rate = 2
    elif weight <= 20:
        base_rate = 5
    elif weight <= 70:
        base_rate = 10
    else:
        base_rate = 20
    
    zone_multiplier = 1
    if destination == "local":
        zone_multiplier = 1
    elif destination == "regional":
        zone_multiplier = 1.5
    else:
        zone_multiplier = 2.5

    price = base_rate * zone_multiplier

    print(f"Customer name: {name}\n"
          f"Package weight (lbs): {weight}\n"
          f"Destination: {destination}\n"
          f"Shipping Price: ${price:.2f}")