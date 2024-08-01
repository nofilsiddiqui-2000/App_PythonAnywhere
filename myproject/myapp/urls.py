# myapp/urls.py
from django.urls import path
from .views import register, user_login, faq_list, home, user_list, profile, submit_faq, approve_faq, event_list

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('faqs/', faq_list, name='faq_list'),
    path('users/', user_list, name='user_list'),
    path('profile/', profile, name='profile'),
    path('submit-faq/', submit_faq, name='submit_faq'),
    path('approve-faq/<int:faq_id>/', approve_faq, name='approve_faq'),
    path('events/', event_list, name='event_list'),
]
