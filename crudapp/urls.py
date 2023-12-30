from django.urls import path
from .views import *

urlpatterns = [

    path('',addshow,name="addshow"),
    path('update/<int:id>',updatedata,name="update"),
    path('delete/<int:id>',deletedata,name="delete"),
    path('login',userlogin,name="login"),
    path('profile',userprofile,name="profile"),
    path('logout',userlogout,name="logout"),
    path('changepass',changepass,name="changepass"),
]
