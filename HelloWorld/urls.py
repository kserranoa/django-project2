from django.urls import path 
from .views import homepageview
from .views import contactspageview

urlpatterns = [
    path('', homepageview.as_view()),
    path('contacts/', contactspageview.as_view(), name = 'contacts')
]