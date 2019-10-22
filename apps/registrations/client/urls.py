from rest_framework.routers import DefaultRouter

from .viewsets import ClientViewSet


router = DefaultRouter()
router.register(r'client', ClientViewSet)
