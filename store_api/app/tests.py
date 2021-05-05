from django.test import TestCase
from app.models import Order

class TestOrderModel(TestCase):
    def setUp(self):
        self.data1 = Order.objects.create(costumer_name='userevertec', costumer_email='user@evertec.com', costumer_mobile='37890001')

    def test_order_model_entry(self):
        """
        Test Order model data insertion field
        """
        data = self.data1
        self.assertTrue(isinstance(data, Order))

