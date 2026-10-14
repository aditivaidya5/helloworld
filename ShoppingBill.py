# Calculate Electronics GST (18%)
def calculateElectronicsGST(a, b):
    return (a + b) * 1.18


# Calculate Fashion GST (13%)
def calculateFashionGST(c, d):
    return (c + d) * 1.13


# Calculate Food GST (7%)
def calculateFoodGST(e):
    return e * 1.07


# Calculate Total Bill after GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


# Calculate Discounted Bill (20% discount)
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount


# Main program: Values passed directly
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 0.20
finalAmount = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {finalAmount:.2f}")