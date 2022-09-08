from django.test import TestCase
from accounts.models import Account


class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.account_data = {
            "username": "ronyelson",
            "password": "1234",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.account: Account = Account.objects.create_user(**cls.account_data)

    def test_account_fields_values(self):

        self.assertEquals(self.account.username, self.account_data["username"])
        self.assertEquals(self.account.first_name, self.account_data["first_name"])
        self.assertEquals(self.account.last_name, self.account_data["last_name"])
        self.assertEquals(self.account.is_seller, self.account_data["is_seller"])
