from django.shortcuts import render
from django.views import View

class Main(View):
    def get(self, request):
        return render(request, 'index.html')
    
class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class SignUp(View):
    def pos 