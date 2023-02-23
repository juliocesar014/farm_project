from django.contrib import admin
from django.urls import include, path
from farm.views import OwnersViewSet, FarmsViewSet, ListFarmOwnerList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('owners', OwnersViewSet, basename='Owners')
router.register('farms', FarmsViewSet, basename='Farms')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('owner/<int:pk>/farms/',ListFarmOwnerList.as_view())
]
