from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer, Staff

class CustomerCreateTest(TestCase):
    def setUp(self):
        # Create a test staff member to be used in the 'updated_by' field
        self.staff = Staff.objects.create(
            staff_id=1,
            first_name='Jane',
            second_name='Doe',
            email='janedoe@example.com',
            position='manager'  # You can set the position if needed
        )

        # Create a test user for login
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_customer(self):
        # Create a new customer by posting the necessary data
        response = self.client.post(reverse('customer-create'), {
            'first_name': 'John',
            'second_name': 'Doe',
            'email': 'johndoe@example.com',
            'updated_by': self.staff.pk  # Pass the staff's pk for 'updated_by'
        })

        # Check if the response is a redirect (302) after successful creation
        self.assertEqual(response.status_code, 302)

        # Check if the customer was actually created in the database
        customer = Customer.objects.first()  # This will fetch the first customer
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.second_name, 'Doe')
        self.assertEqual(customer.email, 'johndoe@example.com')
        self.assertEqual(customer.updated_by, self.staff)