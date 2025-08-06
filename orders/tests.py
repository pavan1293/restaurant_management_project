
from django.test import TestCase
from .models import MenuItem

class MenuItemModelTest(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(
            name="Pasta",
            price=199.99,
            description="Delicious creamy pasta"
        )

    def test_menu_item_creation(self):
        self.assertEqual(self.item.name, "Pasta")
        self.assertEqual(float(self.item.price), 199.99)
        self.assertEqual(self.item.description, "Delicious creamy pasta")
        self.assertEqual(str(self.item), "Pasta")