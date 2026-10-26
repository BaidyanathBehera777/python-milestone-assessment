def calculate_bill(price, quantity):

    total = price * quantity

    if total > 2000:
        discount = total * 0.10
        total = total - discount

    return total


bill = calculate_bill(500, 5)

print("Total Bill:", bill)