import unittest
from myexceptions.cust_not_found_exception import CustomerNotFoundException
from myexceptions.product_not_found_exception import ProductNotFoundException

class TestExceptions(unittest.TestCase):

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            # Simulating the scenario where the exception should be raised
            raise CustomerNotFoundException("Customer ID not found!")

    def test_product_not_found_exception(self):
        with self.assertRaises(ProductNotFoundException):
            # Simulating the scenario where the exception should be raised
            raise ProductNotFoundException("Product ID not found!")

if __name__ == '__main__':
    unittest.main()
