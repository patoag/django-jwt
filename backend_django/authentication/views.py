from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status, filters
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import UserSerializer, UserListSerializer, UserDetailSerializer, UserProfileSerializer
from rest_framework.views import APIView
from .models import UserProfile

# Vista para la creación de usuarios (registro)
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# ViewSet para gestión completa de usuarios (CRUD)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name', 'profile__uuid']
    ordering_fields = ['username', 'date_joined', 'is_active']
    ordering = ['-date_joined']  # Ordenamiento por defecto
    lookup_field = 'pk'  # Puede ser 'id' o 'profile__uuid'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        if self.action in ['retrieve', 'create']:
            return UserDetailSerializer
        return UserSerializer  # Para update y partial_update
    
    def get_permissions(self):
        # Permisos basados en la acción
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]  # Solo administradores
        elif self.action in ['retrieve', 'list']:
            permission_classes = [IsAuthenticated]  # Usuarios autenticados
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_object(self):
        # Permite buscar por UUID o ID
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = self.kwargs[lookup_url_kwarg]
        
        # Intenta determinar si el valor es un UUID
        if len(lookup_value) > 20:  # Heurística simple para identificar un posible UUID
            # Buscar por UUID del perfil
            return get_object_or_404(queryset, profile__uuid=lookup_value)
        else:
            # Buscar por ID normal
            return get_object_or_404(queryset, pk=lookup_value)
            
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def activate(self, request, pk=None):
        """Endpoint para activar/desactivar usuarios"""
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        status_text = 'activado' if user.is_active else 'desactivado'
        return Response({'status': f'Usuario {status_text}'})
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Endpoint para obtener información del usuario autenticado"""
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_me(self, request):
        """Endpoint para que el usuario actualice su propia información"""
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ViewSet para gestionar perfiles directamente por UUID
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'  # Usar UUID como campo de búsqueda