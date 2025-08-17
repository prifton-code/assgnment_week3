def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        return price - discount_amount
    else:
        return price

# Get input from user
price = float(input("Enter item price: "))
discount = float(input("Enter discount percentage: "))

# Calculate and show result
final_price = calculate_discount(price, discount)

if discount >= 20:
    print(f"Price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Price: ${price:.2f}")