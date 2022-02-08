from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.routers import DefaultRouter

# from news.views import NewsViewSet, NewsReviewViewSet, NewsFavouriteViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='deliveryapi',
        default_version='v1',
        description='DeliveryClub'
    ),
    public=True
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)), 
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('order.urls')),


]
