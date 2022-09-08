from django.test import TestCase
from products.models import Product
from accounts.models import Account


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.account_data = {
            "username": "ronyelson",
            "password": "1234",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.account = Account.objects.create_user(**cls.account_data)
        cls.product_data = {
            "description": "Smartband XYZ 3.0",
            "price": 20.99,
            "quantity": 15,
            "seller": cls.account,
        }

        cls.product: Product = Product.objects.create(**cls.product_data)

    def test_product_fields_values(self):
        self.assertEquals(self.product.description, self.product_data["description"])
        self.assertEquals(self.product.price, self.product_data["price"])
        self.assertEquals(self.product.quantity, self.product_data["quantity"])
        self.assertEquals(self.product.seller, self.product_data["seller"])
