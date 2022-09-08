import ipdb
from django.urls import reverse
from accounts.models import Account
from rest_framework.test import APITestCase
from rest_framework.views import status


class SellerTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = "/api/accounts/"
        cls.account_data_seller = {
            "username": "mario",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.account_data_buyer = {
            "username": "luigi",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": False,
        }

    def test_can_register_seller(self):
        response = self.client.post(self.base_url, data=self.account_data_seller)
        # ipdb.set_trace()
        # expected_status_code = 201
        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertTrue(response.data["is_seller"])
        self.assertEqual(expected_status_code, result_status_code)

    def test_can_register_buyer(self):
        response = self.client.post(self.base_url, data=self.account_data_buyer)
        # ipdb.set_trace()
        # expected_status_code = 201
        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(False, response.data["is_seller"])
        self.assertEqual(expected_status_code, result_status_code)

    def test_list_users_without_auth_token(self):
        response = self.client.get(self.base_url)
        self.assertEqual(200, response.status_code)


#     def test_register_librarian_fields(self):
#         response = self.client.post(self.base_url, data=self.librarian_data)
#         # expected_return_fields = ("id", "username", "ssn", "birthdate", "is_superuser")
#         expected_return_fields = ("id", "username", "ssn", "birthdate")

#         self.assertEqual(len(response.data.keys()), 6)

#         # não me garante que SOMENTE as chaves que eu defini vieram na response
#         for expected_field in expected_return_fields:
#             self.assertIn(expected_field, response.data)

#         # verificando se SOMENTE as chaves que eu defini vieram na response
#         result_return_fields = tuple(response.data.keys())

#         self.assertTupleEqual(expected_return_fields, result_return_fields)


class LoginTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.base_url = reverse("login")

        # ipdb.set_trace()

        cls.seller_credentials = {"username": "new_seller", "password": "1234"}
        cls.seller_credentials2 = {"username": "new_seller2", "password": "1234"}

        cls.seller_data = {
            "username": "new_seller",
            "password": "1234",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }

        cls.seller = Account.objects.create_user(**cls.seller_data)

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.base_url, data=self.seller_credentials)
        self.assertEqual(200, response.status_code)

    def test_token_field_is_returned(self):
        response = self.client.post(self.base_url, data=self.seller_credentials)

        # ipdb.set_trace()
        self.assertIn("token", response.data)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(self.base_url, data=self.seller_credentials2)
        self.assertEqual(400, response.status_code)

    def test_token_field_is_not_returned(self):
        response = self.client.post(self.base_url, data=self.seller_credentials2)

        # ipdb.set_trace()
        self.assertNotIn("token", response.data)
