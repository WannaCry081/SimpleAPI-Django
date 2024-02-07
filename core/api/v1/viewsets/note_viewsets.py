from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from core.api.v1.serializers import NoteSerializer, UserSerializer
from core.models import Note

class NoteViewSet(viewsets.GenericViewSet, 
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    