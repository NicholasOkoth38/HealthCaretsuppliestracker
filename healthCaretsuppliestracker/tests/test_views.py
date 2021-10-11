from _typeshed import Self
import pdb
from unittest import result

from rest_framework import test
from .test_setup import TestSetUp

class TestView(TestSetUp):
    def test_user_cannot_register_without_data(self):
        result=self.client.post(self.register_url)
        self.assertEqual(result.status_code, 400)

    def test_user_can_register_correctly(self):
        result=self.client.post(self.register_url, self.user_data, format='json')
        import pdb
        pdb.set_trace()

        self.assertEqual(result.status_code, 201)

