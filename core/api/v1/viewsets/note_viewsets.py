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
    
    
    def list(self, request, *args, **kwargs):
         
        notes = Note.objects.filter(user_id = request.user)
        serializer = NoteSerializer(notes, many = True).data
        return Response(serializer)
        
    
    def create(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        note = serializer.save(user_id=request.user)
        response_data = NoteSerializer(note).data
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
