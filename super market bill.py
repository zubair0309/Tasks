# Supermarket Billing System

products = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Oil": 120,
    "Biscuits": 25
}

print("===================================")
print("       ABC SUPERMARKET")
print("       Guntur, Andhra Pradesh")
print("===================================")

name = input("Enter customer name: ")

cart = {}

while True:
    print("\nAvailable Products:")
    for item, price in products.items():
        print(item, "- Rs.", price)

    choice = input("\nEnter product name (or 'exit' to finish): ").lower()

    if choice.lower() == "exit":
        break

    if choice not in products:
        print("Product not found!")
        continue

    while True:
        quantity = input("Enter quantity: ")

        try:
            quantity = int(quantity)

            if quantity <= 0:
                print("Enter a valid quantity!")
                continue

            break

        except ValueError:
            print("Please enter a valid number!")

    if choice in cart:
        cart[choice] += quantity
    else:
        cart[choice] = quantity

# Bill
print("\n===================================")
print("           ABC SUPERMARKET")
print("          Guntur, AP")
print("===================================")
print("Customer Name:", name)
print("-----------------------------------")
print("Item\tQty\tPrice\tTotal")
print("-----------------------------------")

subtotal = 0

for item, quantity in cart.items():
    price = products[item]
    total = price * quantity
    subtotal += total

    print(item, "\t", quantity, "\t", price, "\t", total)

tax = subtotal * 0.12
grand_total = subtotal + tax

print("-----------------------------------")
print("Total Before Tax : Rs.", subtotal)
print("Tax (12%)        : Rs.", tax)
print("Total Amount     : Rs.", grand_total)
print("===================================")
print("       Thank you for shopping!")
print("===================================")
