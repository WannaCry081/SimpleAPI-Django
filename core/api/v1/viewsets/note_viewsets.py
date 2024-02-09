from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from core.api.v1.serializers import NoteSerializer, UserSerializer
from core.models import Note
from core.versions import LegacyAPIVersion

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class NoteViewSet(viewsets.GenericViewSet, 
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    
    versioning_class = LegacyAPIVersion
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
   
    search_fields = ["title", "body"]
    ordering_fields = ["title", "created_at"]
    ordering = ["-created_at"]
    throttle_classes = [UserRateThrottle]
    
    @swagger_auto_schema(
        operation_summary="List all notes for the authenticated user",
        operation_description="This endpoint returns a list of notes for the authenticated user.",
        responses={
            status.HTTP_200_OK: openapi.Response("Ok", NoteSerializer(many=True))
        },
        produces = ["application/json", "application/xml", "text/html"]
    )
    def list(self, request, *args, **kwargs):
        notes = Note.objects.filter(user_id=request.user)

        page = self.paginate_queryset(notes)
        if page is not None:
            serializer = self.get_serializer(page, many=True).data
            return self.get_paginated_response(serializer)

        serializer = self.get_serializer(notes, many=True).data
        return Response(serializer, status = status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        note = serializer.save(user_id=request.user)
        response_data = self.get_serializer(note).data
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)