from django.urls import path

from .views import Main, ContactUs

urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('register', name='signup')
    path('login', ContactUs.as_view(), name='contact')
]