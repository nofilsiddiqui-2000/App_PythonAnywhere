# myapp/tests/test_forms.py

from django.test import TestCase
from myapp.forms import FAQForm
from django.contrib.auth.models import User

class FAQFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_valid_form(self):
        data = {
            'question': "What is Django?",
            'answer': "Django is a web framework.",
            'submitted_by': self.user.id
        }
        form = FAQForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'question': "",
            'answer': "Django is a web framework.",
            'submitted_by': self.user.id
        }
        form = FAQForm(data=data)
        self.assertFalse(form.is_valid())
