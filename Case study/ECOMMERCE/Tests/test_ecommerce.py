import unittest
from entity.product import Product
from entity.customer import Customer
from dao.order_processor_repository_impl import OrderProcessorRepositoryImpl
from myexceptions.cust_not_found_exception import CustomerNotFoundException
from myexceptions.product_not_found_exception import ProductNotFoundException

class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.repo = OrderProcessorRepositoryImpl()
        self.product = Product(product_id=999, name="Test Mouse", price=299.0, description="Wireless mouse", stock_quantity=5)
        self.customer = Customer(customer_id=999, name="Test User", email="test@example.com", password="test123")

    def test_product_creation(self):
        result = self.repo.create_product(self.product)
        self.assertTrue(result, "Product creation failed!")

    def test_add_product_to_cart(self):
        self.repo.create_customer(self.customer)
        self.repo.create_product(self.product)
        result = self.repo.add_to_cart(self.customer, self.product, 2)
        self.assertTrue(result, "Product not added to cart successfully!")

    def test_place_order(self):
        self.repo.create_customer(self.customer)
        self.repo.create_product(self.product)
        self.repo.add_to_cart(self.customer, self.product, 2)
        result = self.repo.place_order(self.customer, [{self.product: 2}], "Test Address")
        self.assertTrue(result, "Order was not placed successfully!")

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            raise CustomerNotFoundException("Customer ID not found!")

    def test_product_not_found_exception(self):
        with self.assertRaises(ProductNotFoundException):
            raise ProductNotFoundException("Product ID not found!")

if __name__ == "__main__":
    unittest.main()
