

from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', Blog_View, name='blogs'),
    path('blogs/<int:id>/', BlogDetail_View, name='blogs-deatil'),


] 