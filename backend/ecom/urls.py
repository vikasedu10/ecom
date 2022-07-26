from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r'product', views.ProductView, 'product')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/', include("api.urls")),
    
    path('shop/', include('frontend.urls')),
    path('accounts/', include('accounts.urls'), name="accounts"),

    path("", RedirectView.as_view(url="shop/", permanent=True)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

