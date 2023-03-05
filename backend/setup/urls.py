from django.contrib import admin
from django.urls import include, path
from farm.views import OwnersViewSet, FarmsViewSet, ListFarmOwnerList
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Api for Agrosatélite Test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('owners', OwnersViewSet, basename='Owners')
router.register('farms', FarmsViewSet, basename='Farms')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('owner/<int:pk>/farms/',ListFarmOwnerList.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
