from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from  django.shortcuts import render
from django.views import generic
from .models import Applied
from .models import Account_holder







#class IndexView(generic.ListView):
     #template_name = 'music/index.html'

     #def get_queryset(self):
         #return Applied.objects.all()


#class DetailView(generic.DetailView):
 #   model = Applied
  #  template_name = 'music/detail.html'



#def index(request):
    #return HttpResponse("This is from data urls <h1>ALLAH is onee</h1> ")


def index(request):
   return render(request,"sign_up.html")


def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        address=request.POST["address"]
        phone=request.POST["phoneNum"]
        birthdate=request.POST["B_date"]
        n=request.POST["nid"]
        branch=request.POST["branch"]
        passw=request.POST["password"]
        apply=Applied(Name=name,Mail=email,Address=address,Phone=phone,Birth=birthdate,NID=n,Branch=branch,Password=passw)
        apply.save()
    return render(request,'sign_up.html')








#def product_list_view(request):
 #   queryset = Applied.objects.all() # list of objects
  #  context = {
   #     "object_list": queryset
    #}
    #return render(request, "product_lis.html", context)