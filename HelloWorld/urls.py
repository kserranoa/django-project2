from django.urls import path 
from .views import homepageview
from .views import contactspageview
from .views import shoespageview


urlpatterns = [
    path('', homepageview.as_view()),
    path('contacts/', contactspageview.as_view(), name = 'contacts'),
    path('shoes/', shoespageview.as_view(), name = 'shoes')
]