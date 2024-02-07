from django.urls import path, include
from rest_framework import routers
from core.api.v1.viewsets import NoteViewSet 


route = routers.DefaultRouter()
route.register(r"notes", NoteViewSet, basename="notes")


urlpatterns = [
    path("", include(route.urls))
]   