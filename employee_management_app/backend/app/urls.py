from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RackViewSet, SlotViewSet

router = DefaultRouter()
router.register(r'racks', RackViewSet)
router.register(r'slots', SlotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
