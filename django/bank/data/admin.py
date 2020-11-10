from django.contrib import admin
from .models import Applied
from .models import Account_holder,Loan,Deposite,Transfer,Date,Loan_request
from .models import Banker
admin.site.register(Applied)
admin.site.register(Account_holder)
admin.site.register(Banker)
admin.site.register(Deposite)
admin.site.register(Loan)
admin.site.register(Transfer)
admin.site.register(Date)
admin.site.register(Loan_request)

# Register your models here.
