from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('models.urls')),
    path('api/docs/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]