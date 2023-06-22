from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.login, name="login"),
    path('register',views.register, name="register"),
    path('chatbot', login_required(views.chatbot), name="chatbot"),
    path('profile', login_required(views.profile), name="profile"),
    path('logout',views.logout, name="logout"),
    #path('profile', views.EditProfile, name="profile")
]
