from rest_framework import serializers
from core.models import Note

class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Note
        fields = ["id", "title", "body"]
        read_only_fields = ("created_at", "updated_at")
        
            
    