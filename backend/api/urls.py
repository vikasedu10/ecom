from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
urlpatterns = router.urls