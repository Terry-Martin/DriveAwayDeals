from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from sale.models import Customer, Staff, Transaction


class SaleViewsTest(TestCase):

    def setUp(self):
        # Create and save a test staff member (for the updated_by field)
        self.staff = Staff.objects.create(
            first_name='Admin', second_name='User',
            email='admin@example.com', position='manager'
        )
        self.staff.save()
        print(f"Staff ID after creation: {self.staff.staff_id}")

        self.customer = Customer.objects.create(
            first_name='John', second_name='Doe', email='john@example.com',
            updated_by=self.staff
        )
        self.customer.save()
        print(f"Customer ID after creation: {self.customer.customer_id}")

        # Create and save a test staff member for other staff-related tests
        self.staff_member = Staff.objects.create(
            first_name='Jane', second_name='Smith', email='jane@example.com',
            position='manager'
        )
        self.staff_member.save()
        print(f"Staff member ID after creation: {self.staff_member.staff_id}")

        # Create and save a test transaction for customer
        self.transaction = Transaction.objects.create(
            car_registration='AB123CD', price=5000, customer_ID=self.customer
        )
        self.transaction.save()

        # Log in a user to perform requests
        self.user = get_user_model().objects.create_user(
            username='testuser',password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_customer_list_view(self):
        """Test the customer list view"""
        response = self.client.get(reverse('customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')
        self.assertContains(response, 'Doe')

    def test_staff_list_view(self):
        """Test the staff list view"""
        response = self.client.get(reverse('staff_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jane')
        self.assertContains(response, 'Smith')

    def test_transaction_list_view(self):
        """Test the transaction list view"""
        response = self.client.get(reverse('transaction_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AB123CD')
        self.assertContains(response, '5000')

    def test_customer_create_view(self):
        """Test creating a customer"""
        response = self.client.post(reverse('customer-create'), {
            'first_name': 'Alice',
            'second_name': 'Johnson',
            'email': 'alice@example.com',
            'updated_by': self.staff_member.staff_id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Customer.objects.count(), 2)

    def test_staff_create_view(self):
        """Test creating a staff member"""
        response = self.client.post(reverse('staff-create'), {
            'first_name': 'Charlie',
            'second_name': 'Brown',
            'email': 'charlie@example.com',
            'position': 'salesperson'
        })
        # Print response content for debugging purposes
        print(f"Staff creation response: {response.content}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Staff.objects.count(), 3)

    def test_transaction_create_view(self):
        """Test creating a transaction"""
        response = self.client.post(reverse('transaction-create'), {
            'car_registration': 'XY987ZT',
            'price': 3000,
            'customer_ID': self.customer.customer_id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Transaction.objects.count(), 2)
