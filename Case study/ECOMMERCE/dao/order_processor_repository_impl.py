from dao.order_processor_repository import OrderProcessorRepository

class OrderProcessorRepositoryImpl(OrderProcessorRepository):


    def create_product(self, product):
        print("Creating product in DB...")
        return True

    def create_customer(self, customer):
        print("Creating customer in DB...")
        return True

    def delete_product(self, product_id):
        print(f"Deleting product {product_id} from DB...")
        return True

    def delete_customer(self, customer_id):
        print(f"Deleting customer {customer_id} from DB...")
        return True

    def add_to_cart(self, customer, product, quantity):
        print(f"Adding product {product.get_product_id()} to customer {customer.get_customer_id()}'s cart")
        return True

    def remove_from_cart(self, customer, product):
        print(f"Removing product {product.get_product_id()} from customer {customer.get_customer_id()}'s cart")
        return True

    def get_all_from_cart(self, customer):
        print(f"Getting all cart items for customer {customer.get_customer_id()}")
        return []

    def place_order(self, customer, items, shipping_address):
        print(f"Placing order for customer {customer.get_customer_id()} with shipping to {shipping_address}")
        return True

    def get_orders_by_customer(self,customer_id):
        print(f"Getting orders for customer {customer_id}")
        return []









