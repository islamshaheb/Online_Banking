from django.db import models
from django.urls import reverse
from datetime import date
import datetime

#applied pk 01
class Applied(models.Model):
    Name=models.CharField(max_length=250)
    Mail=models.CharField(max_length=250,default='')
    Address=models.TextField(max_length=100)
    Phone=models.CharField(max_length=15,default='')
    Birth=models.CharField(max_length=20,default='')
    NID=models.CharField(max_length=20)
    Branch=models.CharField(max_length=20,default='')
    Password=models.CharField(max_length=20,default='')

   # def get_absolute_uel(self):
      #  return reverse('')

    #
    def __str__(self):
        return str(self.Name)


class Date(models.Model):
    T_date=models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return str(self.T_date)


class Account_holder(models.Model):
    ID=models.ForeignKey(Applied,on_delete=models.CASCADE)
    User_name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.User_name)


class Banker(models.Model):
    Banker_name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    def __str__(self):
        return str(self.Banker_name)

class Loan_request(models.Model):
    Loan_request_name=models.CharField(max_length=100)
    Loan_amount = models.IntegerField()
    def __str__(self):
        return str(self.Loan_request_name)



class Deposite(models.Model):
    Deposite_name= models.CharField(max_length=100,default="")
    Deposite_date = models.DateField(default=datetime.date.today)
    Deposite_amount = models.IntegerField()
    def __str__(self):
        return str(self.Deposite_name)

class Loan(models.Model):
    Loan_name = models.ForeignKey(Account_holder, on_delete=models.CASCADE)
    Loan_date = models.ForeignKey(Date, on_delete =models.CASCADE,default="")
    Loan_amount = models.IntegerField()
    def __str__(self):
        return str(self.Loan_name)



class Transfer(models.Model):
    Transfer_name= models.ForeignKey(Account_holder, on_delete=models.CASCADE)
    Transfer_date=models.DateField(default=datetime.date.today)
    Transfer_amount= models.IntegerField()
    def __str__(self):
        return str(self.Transfer_name)
