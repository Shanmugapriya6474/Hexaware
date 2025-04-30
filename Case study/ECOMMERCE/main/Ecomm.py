from entity.customer import Customer
from entity.product import Product
from dao.order_processor_repository_impl import OrderProcessorRepositoryImpl
from myexceptions.cust_not_found_exception import CustomerNotFoundException
from myexceptions.product_not_found_exception import ProductNotFoundException
from myexceptions.order_not_found_exception import OrderNotFoundException

def main():
    repo = OrderProcessorRepositoryImpl()

    cart = []  # Holds (Product, quantity) tuples temporarily

    while True:
        print("\n=== E-Commerce App Menu ===")
        print("1. Register Customer")
        print("2. Create Product")
        print("3. Delete Product")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. View Customer Order")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cid = int(input("Enter customer ID: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            customer = Customer(cid, name, email, password)
            if repo.create_customer(customer):
                print("Customer registered successfully.")
            else:
                print("Failed to register customer.")

        elif choice == "2":
            pid = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            desc = input("Enter description: ")
            stock = int(input("Enter stock quantity: "))
            product = Product(pid, name, price, desc, stock)
            if repo.create_product(product):
                print("Product created successfully.")
            else:
                print("Failed to create product.")

        elif choice == "3":
            pid = int(input("Enter product ID to delete: "))
            if repo.delete_product(pid):
                print("Product deleted successfully.")
            else:
                print("Failed to delete product.")

        elif choice == "4":
            cid = int(input("Enter your customer ID: "))
            pid = int(input("Enter product ID to add to cart: "))
            qty = int(input("Enter quantity: "))
            customer = Customer(cid)
            product = Product(pid)
            repo.add_to_cart(customer, product, qty)
            cart.append((product, qty))
            print("Product added to cart.")

        elif choice == "5":
            cid = int(input("Enter customer ID to view cart: "))
            customer = Customer(cid)
            items = repo.get_all_from_cart(customer)
            if items:
                print("Cart items:")
                for item in items:
                    print(item)
            else:
                print("Cart is empty.")

        elif choice == "6":
            cid = int(input("Enter your customer ID: "))
            shipping = input("Enter shipping address: ")
            customer = Customer(cid)
            repo.place_order(customer, cart, shipping)
            cart.clear()
            print("Order placed successfully.")

        elif choice == "7":
            cid = int(input("Enter your customer ID: "))
            try:
                orders = repo.get_orders_by_customer(cid)
                print("Orders placed by customer:")
                for order in orders:
                    print(f"Order {order['order_id']}: Product: {order['product_name']}, Quantity: {order['quantity']}")
            except Exception as e:
                print("Error:", e)

        elif choice == "0":
            print("Thank you for using the SP Ecommerce app!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
