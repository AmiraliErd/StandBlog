from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('login', views.userlogin, name="login"),
    path('logout', views.userlogout, name="logout"),
    path('register', views.Register, name="register")
]
