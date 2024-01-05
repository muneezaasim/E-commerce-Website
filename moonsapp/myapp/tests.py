from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class SignupLoginTests(TestCase):
    def test_signup_view(self):
        test_username = 'testuser'
        test_email = 'testuser@example.com'
        test_password = 'testpassword'

        response = self.client.post(reverse('register'), {'username':test_username, 'email': test_email ,'password':test_password})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        print(User.objects.all())

    def test_login_view(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        
        response = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'testpassword'}
        )
    
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        print(User.objects.all())
   

