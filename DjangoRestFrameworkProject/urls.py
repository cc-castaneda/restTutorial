from django.contrib import admin
from django.urls import path, include

'''
#from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets

# Forma genérica de usar las vistas para crear usuarios

# define la representacion del API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'username', 'is_staff']

#  define el comportamiento de la vista
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ruta facil automática determoinada por URL conf 
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restFramework.urls')),
#    path(r'', include(router.urls)),
#    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]