from rest_framework import serializers                                                                              # type: ignore
from .models import UploadedFile
from djoser.serializers import UserCreateSerializer                                                                  # type: ignore
from .models import CustomUser

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at']
        
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'email', 'password') 


