from rest_framework import serializers
from core.models import Note

class NoteSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    
    class Meta:
        
        model = Note
        fields = ["id", "title", "body", "user"]
        read_only_fields = ("created_at", "updated_at")
        
    
    def get_user(self, instance):
        
        if instance:
            user_instance = instance.user
            return  {
                "id" : user_instance.id,
                "username" : user_instance.username,
                "email" : user_instance.email
            }
        else:
            return None
    
    
    def to_representation(self, instance):
        
        data = super().to_representation(instance)
        data["user"] = self.get_user(instance)
        return data
    