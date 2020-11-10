from django.http import HttpResponse
from django.shortcuts import render
from data.models import Applied
from data.models import Account_holder
from data.models import Loan_request,Loan,Deposite, Transfer
#def ab(request):
   #print(Applied.objects.all)
def homepage(request):
   return render(request,"home.html")

def useropt(request):
   return render(request,"User_opt.html")

def contact(request):
   return render(request,"contact.html")

def login(request):
   return render(request,"login.html")

def admin(request):
   return render(request,"Admin_menu.html")




context={}

def login(request):

   request.session['user']=" "
  # context = {}
   if request.method == 'POST':
      user_name = request.POST["username"]
      password = request.POST["pass"]
      if (Account_holder.objects.filter(User_name=user_name) and Applied.objects.filter(Password=password)):
        # x=Applied.objects.filter(id(0))
         request.session['user'] = user_name
         print("ok fine",user_name,"ok")
         #user=request.session['user']
         context['userName'] = request.session['user']
         data=Applied.objects.filter(Password=password)
         #data=Applied.objects.all
         #place = Applied.objects.get(password)
         # print(place.id)
         #data=place.id
         data2 = Loan_request.objects.filter(Loan_request_name=user_name)
         data3 = Deposite.objects.filter(Deposite_name=user_name)
         data4 = Transfer.objects.filter(Transfer_name__User_name=user_name)
         stu = {
          "number": data,
          "number2": data2,
          "number3": data3,
          "number4": data4,
              }

     # return render_to_response("login/profile.html", stu)
         return render(request,'User_menu.html',stu)

      else:
         return render(request, 'about.html', {'print': "username and password is incorrect"})

   return render(request, 'login.html', {'userName': request.session['user']})


def logout(request):
    request.session['user'] = None
    return render(request, 'login.html', {'userName': request.session['user']})


def loan(request):
    if request.method=="POST":
        name=request.POST["username"]
        email=request.POST["amount"]

        object=Loan_request(Loan_request_name=name,Loan_amount=email)
        object.save()
    return render(request,'loan.html')



def depo(request):
    if request.method=="POST":
        user=request.POST["username"]
        da=request.POST["date"]
        am=request.POST["amount"]
        ob=Deposite(Deposite_name=user,Deposite_date=da,Deposite_amount=am)
        print(user,da,am)
        ob.save()
    return render(request,"deposit .html")

def transfer(request):
    if request.method=="POST":
        us=request.POST["to"]
        data3=Account_holder.objects.filter(User_name=us)[0]
        dat=request.POST["date"]
        amo=request.POST["amount"]
        obj=Transfer(Transfer_name=data3,Transfer_date=dat,Transfer_amount=amo)
        print(us,dat,amo)
        obj.save()
    return render(request,"transfer.html")