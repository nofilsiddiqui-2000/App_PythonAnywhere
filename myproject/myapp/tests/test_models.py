# myapp/tests/test_models.py

from django.test import TestCase
from django.contrib.auth.models import User
from myapp.models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", submitted_by=self.user)

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a web framework.")
        self.assertEqual(self.faq.submitted_by.username, 'testuser')

    def test_str_method(self):
        self.assertEqual(str(self.faq), "What is Django?")
