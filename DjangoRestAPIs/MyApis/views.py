from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from MyApis.models import MyUser
from MyApis.serializers import MyUserSerializer


class MyUserViewset(ModelViewSet):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('user created successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        username = request.query_params.get('username', None)
        if username:
            data = MyUser.objects.get(username=username)
            serializer = MyUserSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('username is required in query param', status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        username = request.data['username']
        updated_username = request.data['new_username']
        if username:
            MyUser.objects.filter(username=username).update(username=updated_username)
            return Response('username is updated successfully', status=status.HTTP_200_OK)
        else:
            return Response('username is required in body', status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        username = request.query_params.get('username', None)
        if username:
            MyUser.objects.get(username=username).delete()
            return Response('user deleted successfully', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('username is required in query param', status=status.HTTP_400_BAD_REQUEST)
