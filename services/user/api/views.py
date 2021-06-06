from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import CustomUser
from api.serializers import UserSerializer


# TODO – Test view; To delete later
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, ])
@api_view(http_method_names=["GET"])
def test_endpoint(request):
    if request.method == 'GET':
        queryset = CustomUser.objects.all()
        if queryset.count() != 0:
            serializer_class = UserSerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:
            return Response(status=200)
