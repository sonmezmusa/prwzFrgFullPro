from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/', newsP, name='news'),
    path('newsdate/<int:year>', newsDate, name='newsdate'),
    path('contact/', contact, name='contact'),
    path('signup/', register, name='register'),
    path('addUser/', addUser, name='addUser'),
    path('modelform/', modelform, name='modelform'),
    path('addmodelform/', addModelForm, name='addmodelform'),
]