from flask import json,jsonify
from my_app.models import User
import unittest as unittest

class UserApiTest(unittest.TestCase):
    def test_addnewuser(self):
        """Test user model exists"""
        self.assertTrue(User)