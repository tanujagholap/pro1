from django.urls import path
from .views import *


urlpatterns = [
    path('', create_view, name='create_urls'),
    path('show/', show_view, name='show_urls'),
    path('update/<int:pk>/', update_view, name='update_urls'),
    path('delete/<int:pk>/', delete_view, name='delete_urls')

]