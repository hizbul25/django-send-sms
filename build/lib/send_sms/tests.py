from django.core.exceptions import ValidationError
from django.test import TestCase

from send_sms.views import validate_receiver_nos

# Create your tests here.


class SMSTestCase(TestCase):
    def test_validate_receiver_nos(self):
        response = validate_receiver_nos(['01671589788', '01671589799'])
        self.assertEqual(len(response), 2)
        with self.assertRaises(ValidationError, msg='Please enter valid mobile nos'):
            validate_receiver_nos([''])
