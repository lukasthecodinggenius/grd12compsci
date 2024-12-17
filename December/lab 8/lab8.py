inventory = [
    {"id": 1, "name": "Laptop", "price": 999.99},  
    {"id": 2, "name": "Smartphone", "price": 599.99},  
    {"id": 3, "name": "Headphones", "price": 89.99}  
]

cart = []  # List to store cart items

def display_products():
    # Display products in inventory
    for product in inventory:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")

def add_to_cart():
    try:
        # Prompt user for product ID and quantity
        product_id = int(input("Enter the product ID to add to cart: "))
        quantity = int(input("Enter the quantity: "))
        product = None
        # Find the product in inventory by ID
        for p in inventory:
            if p["id"] == product_id:
                product = p
                break
        if product:
            item_in_cart = None
            # Check if the product is already in the cart
            for item in cart:
                if item["id"] == product_id:
                    item_in_cart = item
                    break
            if item_in_cart:
                # Increase quantity if already in cart
                item_in_cart["quantity"] += quantity
            else:
                # Add new product to the cart
                cart.append({"id": product["id"], "name": product["name"], "price": product["price"], "quantity": quantity})
        else:
            print("Invalid product ID.")  # Error if product not found
    except ValueError:
        print("Invalid input. Please enter numeric values.")  # Handle non-numeric input

def view_cart():
    if not cart:
        # Inform user if cart is empty
        print("Your cart is empty.")
    else:
        total = 0  # Initialize total cost
        for item in cart:
            # Calculate total for each item
            item_total = item["quantity"] * item["price"]
            total += item_total  # Add to overall total
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Total: ${item_total:.2f}")
        print(f"Overall Total: ${total:.2f}")  # Display overall total

def remove_from_cart():
    try:
        # Prompt user for product ID to remove
        product_id = int(input("Enter the product ID to remove from cart: "))
        item = None
        # Find the product in the cart by ID
        for i in cart:
            if i["id"] == product_id:
                item = i
                break
        if item:
            cart.remove(item)  # Remove the product from the cart
            print(f"Removed {item['name']} from your cart.")
        else:
            print("Item not found in the cart.")  # Error if product not in cart
    except ValueError:
        print("Invalid input. Please enter numeric values.")  # Handle non-numeric input

def complete_purchase():
    if not cart:
        # Inform user if cart is empty
        print("Your cart is empty. Cannot complete purchase.")
    else:
        # Calculate total price of all items in the cart
        total = sum(item["quantity"] * item["price"] for item in cart)
        print(f"Your total is: ${total:.2f}")
        confirm = input("Do you want to proceed with the purchase? (yes/no): ").lower()
        if confirm == "yes":
            print("Purchase successful! Thank you for shopping.")
            cart.clear()  # Clear the cart after purchase
        else:
            print("Purchase canceled.")

def main_menu():
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Complete Purchase")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_products()  # View products
        elif choice == "2":
            add_to_cart()  # Add product to cart
        elif choice == "3":
            view_cart()  # View cart contents
        elif choice == "4":
            remove_from_cart()  # Remove product from cart
        elif choice == "5":
            complete_purchase()  # Complete the purchase
        elif choice == "6":
            print("Thank you for visiting the store. Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choice

main_menu()  # Start the program
