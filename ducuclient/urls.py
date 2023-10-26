from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('explorer/', include('explorer.urls')),
    path('cliente/', include('cliente.urls')),
]

urlpatterns += staticfiles_urlpatterns()
