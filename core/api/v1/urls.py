from rest_framework import routers
from core.api.v1.viewsets import *


route = routers.DefaultRouter()
route.register(r"notes", NoteViewSet, basename="notes")
