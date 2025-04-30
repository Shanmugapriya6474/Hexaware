import unittest
from entity.customer import Customer
from entity.product import Product
from dao.order_processor_repository_impl import OrderProcessorRepositoryImpl

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.repo = OrderProcessorRepositoryImpl()
        self.customer = Customer(customer_id=1001, name="Test User", email="test@example.com", password="pass123")
        self.product = Product(product_id=5678, name="Test Mouse", price=299.99, description="Wireless Mouse", stock_quantity=15)

        # Make sure the customer and product exist before testing add to cart
        self.repo.create_customer(self.customer)
        self.repo.create_product(self.product)

    def test_add_to_cart(self):
        result = self.repo.add_to_cart(self.customer, self.product, quantity=2)
        self.assertTrue(result, "Failed to add product to cart")

if __name__ == '__main__':
    unittest.main()
