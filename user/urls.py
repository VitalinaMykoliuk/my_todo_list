from django.contrib import admin
from django.urls import path
from user.views import RegistrationUserView, MainUserView, LoginUserView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'


urlpatterns = [
    path('', MainUserView.as_view(), name='main'),
    path('register/', RegistrationUserView.as_view(), name='reg'),
    path('login/', LoginUserView.as_view(), name='log'),

]


