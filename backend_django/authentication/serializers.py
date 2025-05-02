from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['uuid', 'bio', 'avatar', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    uuid = serializers.SerializerMethodField()
    bio = serializers.CharField(source='profile.bio', required=False, allow_blank=True)
    avatar = serializers.ImageField(source='profile.avatar', required=False, allow_null=True)
    
    class Meta:
        model = User
        fields = ['id', 'uuid', 'username', 'email', 'first_name', 'last_name', 'password', 
                 'bio', 'avatar', 'profile', 'date_joined', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'date_joined': {'read_only': True},
        }
    
    def get_uuid(self, obj):
        return obj.profile.uuid if hasattr(obj, 'profile') else None

    def create(self, validated_data):
        profile_data = {}
        # Extraer datos del perfil
        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
        # Para campos individuales de perfil pasados directamente
        if 'bio' in validated_data.get('profile', {}):
            profile_data['bio'] = validated_data['profile'].pop('bio')
        if 'avatar' in validated_data.get('profile', {}):
            profile_data['avatar'] = validated_data['profile'].pop('avatar')
            
        # Crear el usuario
        user = User.objects.create_user(**validated_data)
        
        # Actualizar perfil con datos extra si los hay
        if profile_data:
            for key, value in profile_data.items():
                setattr(user.profile, key, value)
            user.profile.save()
        
        return user
        
    def update(self, instance, validated_data):
        # Extraer y manejar datos del perfil
        profile_data = {}
        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
        
        # Manejar campos individuales de perfil pasados directamente
        if 'bio' in validated_data:
            profile_data['bio'] = validated_data.pop('bio')
        if 'avatar' in validated_data:
            profile_data['avatar'] = validated_data.pop('avatar')
            
        # Manejar contraseña separadamente
        password = validated_data.pop('password', None)
        
        # Actualizar campos del usuario
        for key, value in validated_data.items():
            setattr(instance, key, value)
            
        # Actualizar contraseña si se proporcionó
        if password:
            instance.set_password(password)
            
        # Guardar usuario
        instance.save()
        
        # Actualizar perfil
        if profile_data and hasattr(instance, 'profile'):
            for key, value in profile_data.items():
                setattr(instance.profile, key, value)
            instance.profile.save()
            
        return instance

class UserListSerializer(serializers.ModelSerializer):
    """Serializer para listar usuarios con información limitada"""
    uuid = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'uuid', 'username', 'email', 'first_name', 'last_name', 'is_active']
    
    def get_uuid(self, obj):
        return obj.profile.uuid if hasattr(obj, 'profile') else None

class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer para detalles completos del usuario"""
    profile = UserProfileSerializer(read_only=True)
    uuid = serializers.SerializerMethodField()
    bio = serializers.CharField(source='profile.bio', required=False, read_only=True)
    avatar = serializers.ImageField(source='profile.avatar', required=False, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'uuid', 'username', 'email', 'first_name', 'last_name', 
                 'bio', 'avatar', 'profile', 'date_joined', 'last_login', 'is_active']
        read_only_fields = ['id', 'date_joined', 'last_login']
        
    def get_uuid(self, obj):
        return obj.profile.uuid if hasattr(obj, 'profile') else None