def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying the discount.
    Only applies the discount if discount_percent is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Prompt the user for input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"Final price after {discount_percentage}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values.")
