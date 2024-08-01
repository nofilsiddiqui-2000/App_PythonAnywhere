# myapp/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.models import FAQ

class FAQViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", submitted_by=self.user)

    def test_faq_list_view(self):
        response = self.client.get(reverse('faq_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.faq.question)
        self.assertTemplateUsed(response, 'faq_list.html')
