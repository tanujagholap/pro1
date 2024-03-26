from django.urls import path
from .views import *


urlpatterns = [
    path('login/', user_login, name='login_urls'),
    path('logout/', user_logout,  name='logout_urls'),
    path('sign_up/', sign_up,  name='signup_urls'),
    path('cpass/', change_password, name='cpass_urls')

]