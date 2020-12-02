from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jsonHello/', include('jsonHelloWorld.urls')),
    path('helloWorld/', include('polls.urls')),
    path('admin/', admin.site.urls),    
]
