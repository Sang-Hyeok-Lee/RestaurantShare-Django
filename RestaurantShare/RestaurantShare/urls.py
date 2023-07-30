from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shareRes.urls')),
    path('sendEmail/', include('sendEmail.urls')),
    path('admin/', admin.site.urls),
]
