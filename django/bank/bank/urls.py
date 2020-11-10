from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import  views

urlpatterns = [
  path('admin',admin.site.urls),
  path('',views.homepage),
  path('homepage',views.homepage),
  path('useropt',views.useropt),
  path('contact',views.contact),
  path('admin1',views.admin),
  path('loan',views.loan,name='loan'),
  path('depo',views.depo,name='depo'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('transfer',views.transfer,name='transfer'),


  path('sign_up',include('data.urls')),


]

urlpatterns +=staticfiles_urlpatterns()
if settings.DEBUG:
  urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)