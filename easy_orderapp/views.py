from django.shortcuts import render
from easy_orderapp.models import easy_orderapp,shopproduct,UserUpdateForms
# Create your views here.                                                                                                                                                                                                                                                                                                                                                    
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def blogview(request):
    return render(request, "blogview.html")
def contact(request):
    return render(request, "contact.html")
def login(request):
    return render(request, "log in.html")
def signup(request):
    return render(request, "signup.html")

def shop(request):
    itms = shopproduct.objects.all()
    q={"itms": itms}
    return render(request,"shop.html",q)
def usersignin(request):
    context={}
    return render(request,"user.html",context)

    
