from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('enquire/', views.enquire, name='enquire'),
    path('logout/', views.logout_view, name='logout'),
    path('formsuccess/', views.formsuccess, name='formsuccess'),

]