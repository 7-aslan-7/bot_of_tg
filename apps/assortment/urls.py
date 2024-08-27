from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, NewArrivalsList

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/new-arrivals/', NewArrivalsList.as_view(), name='new-arrivals'),
]
