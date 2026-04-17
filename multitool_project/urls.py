from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('image_tools.urls')),
    path('admin/', admin.site.urls),
]
