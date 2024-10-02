
from django.contrib import admin
from django.urls import include, path

from home.views import index

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', index),  # Directly map the root URL to the index view
]
