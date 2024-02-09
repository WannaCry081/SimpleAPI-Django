from django.urls import path, include
from core.api.v1 import route as api_v1


urlpatterns = [
    path("v1/", include(api_v1.urls))  
]