from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, decorators, response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HealthViewSet(viewsets.ViewSet):

    permission_classes = (AllowAny, )

    def list(self, request, format=None):

        ## make sure we can connect to the database
        all_statuses = []
        status = "up"

        db_status = self.__can_connect_to_db()

        all_statuses.append(db_status)

        if "down" in all_statuses:
            status = "down"

        data = {
            "data": {
                "explorer" : "/api-explorer",
            },
            "status": {
                "db": db_status,
                "status": status
            }
        }
        return response.Response(data)

    def __can_connect_to_db(self):
        try:
            user = User.objects.first()
            return "up"
        except Exception:
            return "down"

            
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'health', HealthViewSet, base_name='health')
