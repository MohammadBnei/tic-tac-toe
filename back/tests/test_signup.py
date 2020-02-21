import unittest
import json

from tests.BaseCase import BaseCase

class SignupTest(BaseCase):

    def test_successful_sigup(self):
        # Given
        payload = json.dumps({
            "email": "test@case.com",
            "password": "testIngPass"
        })

        # When
        response = self.app.post('/api/auth/signup', headers={
            "Content-Type": "application/json"
        }, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)