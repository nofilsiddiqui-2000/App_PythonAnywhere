from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", submitted_by=self.user)

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a web framework.")
        self.assertEqual(self.faq.submitted_by.username, 'testuser')

class FAQViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", submitted_by=self.user)

    def test_faq_list_view(self):
        response = self.client.get(reverse('faq_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.faq.question)
        self.assertTemplateUsed(response, 'faq_list.html')
