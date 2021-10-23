from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Api de prueba"""

    serializer_class = serializers.HelloSerializer

    def get(self, req, format=None):
        """Retornar lista de caracteristicas"""
        an_apiview = [
            'Hola que tal',
            'como te va',
            'tiene un momento',
            'pa yo molestar'
        ]

        return Response({'res': 'hello', 'an_apiview': an_apiview })

    def post(self, req):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



