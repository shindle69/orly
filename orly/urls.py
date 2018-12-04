from django.contrib import admin
from django.urls import path , include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cover/', include('cover.urls')),
    path('',lambda r:redirect('cover:index')),
]
