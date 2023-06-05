from rest_framework import status
from rest_framework.test import APITestCase

class CreateUpdateImageTagTests(APITestCase):

    def test_farmer_create(self):
        """
            Create Farmer record.
        """
        data = {
            "name": "Doga2",
            "phone": "9872856544",
            "village": "Jokar",
            "block_tahsil": "Bhadetha",
            "district": "Ruderpur",
            "state": "KA",
            "country": "IN",
            "latitude": 21.427503,
            "longitude": 80.627295,
            "amount": 333.0,
            "remarks": "sdf",
            "uid": "w",
            "gp": "345",
            "year": "2023"
        }
        res = self.client.post('/api/v1/farmer/create/', data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_farmer_list(self):
        """
            Test list API.
        """
        url = '/api/v1/farmers/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
            