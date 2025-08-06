
from django.test import TestCase
from .models import MenuItem

class MenuItemModelTest(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(
            name="Veg Biryani",
            price=180.00,
            description="Aromatic rice with spices and vegetables"
        )

    def test_menu_item_content(self):
        self.assertEqual(self.item.name, "Veg Biryani")
        self.assertEqual(float(self.item.price), 180.00)
        self.assertEqual(self.item.description, "Aromatic rice with spices and vegetables")
        self.assertEqual(str(self.item), "Veg Biryani")