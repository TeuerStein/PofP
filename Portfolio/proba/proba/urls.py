from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('portfol/', include('portfol.urls')),
    path('admin/', admin.site.urls),
]
