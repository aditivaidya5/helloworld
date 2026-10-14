
def calculateResidentialSurcharge(a):
    return a + (a * 5 / 100)


def calculateCommercialSurcharge(b):
    return b + (b * 10 / 100)


def calculateIndustrialSurcharge(c):
    return c + (c * 15 / 100)


def totalBill(a, b, c):
    residential = calculateResidentialSurcharge(a)
    commercial = calculateCommercialSurcharge(b)
    industrial = calculateIndustrialSurcharge(c)

    return residential + commercial + industrial


def calculateDiscountedBill(a, b, c):
    total = totalBill(a, b, c)
    discount = total * 10 / 100

    return total - discount


# Direct values
a = 1000
b = 2000
c = 3000

total = totalBill(a, b, c)
discount = total * 10 / 100
final_amount = calculateDiscountedBill(a, b, c)

print(f"Total after surcharge = ₹{total:.2f}")
print(f"Discount = ₹{discount:.2f}")
print(f"Final payable amount = ₹{final_amount:.2f}")
