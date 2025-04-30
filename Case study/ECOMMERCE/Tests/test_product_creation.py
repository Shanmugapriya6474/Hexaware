import unittest
from entity.product import Product
from dao.order_processor_repository_impl import OrderProcessorRepositoryImpl

class TestProductCreation(unittest.TestCase):
    def setUp(self):
        self.repo = OrderProcessorRepositoryImpl()
        self.product = Product(
            product_id=1234,
            name="Test Headphones",
            price=799.99,
            description="Bluetooth over-ear headphones",
            stock_quantity=20
        )

    def test_create_product(self):
        result = self.repo.create_product(self.product)
        self.assertTrue(result, "Product creation failed!")

if __name__ == '__main__':
    unittest.main()
