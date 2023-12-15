from django.test import TestCase, Client
from restaurant.models import Menu
from django.contrib.auth.models import User
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status

# class MenuViewTest(TestCase):
#      def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )
        
#         self.pizza = Menu.objects.create(title='Pizza', price=12.99, inventory=10)
#         self.burger = Menu.objects.create(title='Burger', price=8.99, inventory=5)
#         self.pasta = Menu.objects.create(title='Pasta', price=15.99, inventory=7)



#      def test_getall(self):
#         self.loginAsTestUser()
#         response = self.client.get(reverse('menu'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#         menu = Menu.objects.all()
#         serializer = MenuSerializer(menu, many=True)
#         self.assertEqual(response.data, serializer.data)


class MenuViewTest(TestCase):
    def setUp(self):
        self.create_menu_items()
        super().setUp()

    def test_list(self):
        response = self.client.get(reverse('api:menu'))
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
        
    def test_create(self):
        data = {'title': 'latte', 'price': 2.99, 'inventory': 5}
        response = self.client.post(reverse('api:menu'), data=data)
        serializer = MenuSerializer(Menu.objects.get(title='latte'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)

    def test_delete(self):
        response = self.client.delete(reverse('api:menu-detail', kwargs={'pk': self.menu_item.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
        self.assertEqual(Menu.objects.filter(pk=self.menu_item.pk).exists(), False)