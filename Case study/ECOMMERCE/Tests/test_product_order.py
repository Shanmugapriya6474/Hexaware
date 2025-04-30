import unittest
from entity.customer import Customer
from entity.product import Product
from dao.order_processor_repository_impl import OrderProcessorRepositoryImpl


class TestPlaceOrder(unittest.TestCase):
    def setUp(self):
        self.repo = OrderProcessorRepositoryImpl()

        # Sample customer and product
        self.customer = Customer(customer_id=2001, name="Order Tester", email="order@test.com", password="orderpass")
        self.product = Product(product_id=3010, name="Test Charger", price=499.0, description="Fast charger",
                               stock_quantity=10)

        # Ensure they exist
        self.repo.create_customer(self.customer)
        self.repo.create_product(self.product)
        self.repo.add_to_cart(self.customer, self.product, quantity=1)

    def test_place_order(self):
        items = [{self.product: 1}]
        result = self.repo.place_order(self.customer, items, shipping_address="Test City")
        self.assertTrue(result, "Failed to place order")


if __name__ == '__main__':
    unittest.main()
