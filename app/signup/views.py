from django.http import HttpResponse
from django.shortcuts import redirect 
from django.views import View
from django.template import loader
from signup.forms import SignUpForm
from clients.models import ClientModel
# Create your views here.

class SignupView(View):
    def get(self, request):
        template = loader.get_template("register.html")
        context = {"forms": SignUpForm}
        return HttpResponse(template.render(context, request))
    def post(self, request):
        user_data = {
            "first_name":request.POST.get("first_name"),
            "last_name":request.POST.get("last_name"),
            "password":request.POST.get("password"),
            "username":request.POST.get("email"),
        } 
        ClientModel.objects.create_user(**user_data)
        return redirect("/login/")

    
        
    