from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profile_api import serializers

class HelloAPIView(APIView):
    """ API View """

    serializers_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """ Returns lit of APIView Features """
        an_apiview = [
        'Uses HTTP MEthod as functions',
        'Is similar to traditional Django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URL'
        ]
        return Response({"an_apiview":an_apiview, 'message': 'Hello'})

    def post(self, request):
        """ Returns lit of APIView Features """
        serialize = self.serializers_class(data = request.data)

        if serialize.is_valid():
            name = serialize.validated_data.get('name')
            message = f'Hello World:{name}'
            return Response({'message': message})
        else:
            return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk =None):
        return Response({'method': 'PUT'})


    def delete(self, request, pk =None):
        return Response({'method': 'DELTE'})

    def patch(self, request, pk =None):
        return Response({'method': 'PATCH'})


class HelloViewSet(viewsets.ViewSet):

    serializers_class = serializers.HelloSerializers

    def list(self, request):
        """Hello Message"""

        an_apiview = [
        'Uses HView',
        'Is similar to traditional Django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URL'
        ]
        return Response({"an_apiview":an_apiview, 'message': 'Hello'})

    def create(self, request):
        """Create"""

        serialize = self.serializers_class(data = request.data)

        if serialize.is_valid():
            name = serialize.validated_data.get('name')
            message = f'Hello World:{name}'
            return Response({'message': message})
        else:
            return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Response """

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Update """

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Partial Update """

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """delete """

        return Response({'http_method':'DELETE'})
