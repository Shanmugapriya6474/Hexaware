from dao.order_processor_repository_impl import OrderProcessorRepositoryImpl
from entity.product import Product
from entity.customer import Customer

# Create the repository instance
repo = OrderProcessorRepositoryImpl()

# Create a test product and customer
product = Product(product_id=1, name="Laptop", price=50000, description="Gaming Laptop", stock_quantity=10)
customer = Customer(customer_id=1, name="John Doe", email="john@example.com", password="1234")

# Call some methods to test
repo.create_product(product)
repo.create_customer(customer)
repo.add_to_cart(customer, product, quantity=2)
repo.get_all_from_cart(customer)

