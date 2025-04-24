from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail
from models.payment import Payment
from dao.customer_dao import CustomerDAO
from dao.product_dao import ProductDAO
from dao.order_dao import OrderDAO
from dao.inventory_dao import InventoryDAO
from dao.reporting_dao import ReportingDAO  # Import ReportingDAO for reporting functionality
from dao.reporting_dao import ReportingDAO  # Import ReportingDAO for reporting functionality
from services.product_service import ProductService  # Import the ProductService for search and recommendations
from services.payment_service import PaymentService  # Import the PaymentService for payment processing
from db.database_connector import DatabaseConnector # Database connection for ProductService


def main():
    database_connector = DatabaseConnector()  # Create a DB connection instance
    customer_dao = CustomerDAO()
    product_dao = ProductDAO()
    order_dao = OrderDAO()
    inventory_dao = InventoryDAO()
    reporting_dao = ReportingDAO()
    product_service = ProductService(database_connector)  # Create the ProductService instance
    payment_service = PaymentService(database_connector)  # Create the PaymentService instance

    print("Welcome to Royal TechShop")

    while True:
        print("\nMenu:")
        print("1. Register Customer")
        print("2. Add Product")
        print("3. Place Order")
        print("4. Check Order Status")
        print("5. Update Inventory")
        print("6. Discontinue Product")
        print("7. Get Total Sales by Date")  # Option to fetch total sales by date
        print("8. Update Customer Information")  # Option to update customer info
        print("9. Search Products")  # Option for product search
        print("10. Product Recommendations")  # Option for product recommendations
        print("11. Process Payment")  # Option for processing payment
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            customer = Customer(name=name, email=email, phone=phone)
            customer_dao.add_customer(customer)
            print("Customer registered successfully.")

        elif choice == 2:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            description = input("Enter product description: ")
            stock = int(input("Enter stock quantity: "))
            product = Product(name=name, price=price, description=description, stock=stock)
            inventory_dao.add_product(product)
            print("Product added to inventory successfully")

        elif choice == 3:
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter product price: "))
            total_amount = quantity * price
            order = Order(customer_id=customer_id, total_amount=total_amount, status="Processing")
            order_details = [OrderDetail(product_id=product_id, quantity=quantity, price=price)]
            order_dao.place_order(order, order_details)
            print("Order placed successfully ")

        elif choice == 4:
            order_id = int(input("Enter Order ID: "))
            status = order_dao.get_order_status(order_id)
            print(f"Order Status for Order ID {order_id}: {status}")

        elif choice == 5:
            product_id = int(input("Enter product ID: "))
            new_stock = int(input("Enter new stock quantity: "))
            inventory_dao.update_stock(product_id, new_stock)
            print("Inventory updated successfully")

        elif choice == 6:
            product_id = int(input("Enter product ID to discontinue: "))
            inventory_dao.discontinue_product(product_id)
            print("Product discontinued successfully")

        elif choice == 7:  # Get total sales by date
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")
            report = reporting_dao.get_total_sales_by_date(start, end)
            if report:
                for row in report:
                    print(f"Date: {row[0]} | Total Sales: ₹{row[1]}")
            else:
                print("No sales data found for the given date range.")

        elif choice == 8:  # Update customer information
            cust_id = int(input("Enter Customer ID: "))
            new_email = input("Enter new email (leave blank to skip): ").strip()
            new_phone = input("Enter new phone (leave blank to skip): ").strip()

            dao = CustomerDAO()
            dao.update_customer_info(customer_id=cust_id, email=new_email or None, phone=new_phone or None)
            print("Customer information updated successfully.")

        elif choice == 9:  # Search Products
            search_name = input("Enter product name to search (leave blank for no name filter): ").strip()
            search_category = input("Enter product category to search (leave blank for no category filter): ").strip()
            products = product_service.search_products(name=search_name, category=search_category)
            if products:
                for product in products:
                    print(f"Found product: {product.name} | Price: ₹{product.price} | Category: {product.category}")
            else:
                print("No products found based on the search criteria.")

        elif choice == 10:  # Product Recommendations
            customer_id = int(input("Enter customer ID for product recommendations: "))
            recommendations = product_service.recommend_products(customer_id)
            if recommendations:
                for product in recommendations:
                    print(
                        f"Recommended product: {product.name} | Price: ₹{product.price} | Category: {product.category}")
            else:
                print("No recommendations found for the given customer.")

        elif choice == 11:  # Process Payment
            order_id = int(input("Enter the order ID for payment processing: "))
            payment_method = input("Enter payment method (e.g., Credit Card, PayPal, etc.): ").strip()
            amount = float(input("Enter payment amount: "))

            # Create payment record
            payment = Payment(order_id=order_id, amount=amount, payment_method=payment_method,payment_status="Successful")
            if payment_service.process_payment(payment):
                print(f"Payment of ₹{amount} processed successfully for Order ID {order_id}.")
            else:
                print("Payment processing failed. Please try again.")

        elif choice == 12:
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()