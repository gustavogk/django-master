from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.api.views import CarViewSet, CarListCreateView, CarRetrieveUpdateDestroyView

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cars-api/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars-api/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car-detail'),
]
