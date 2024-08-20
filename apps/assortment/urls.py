from django.urls import path
from .views import NewArrivalsList

urlpatterns = [
    path('api/new-arrivals/', NewArrivalsList.as_view(), name='new-arrivals'),
]
