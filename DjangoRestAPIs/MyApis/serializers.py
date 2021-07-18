from rest_framework.serializers import ModelSerializer
from MyApis.models import MyUser


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
