from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Scope, Weapon


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        fields = ['id', 'name', 'magnitude', 'sell_price']

class ScopeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        fields = ['name','id',]

class WeaponSerializer(serializers.ModelSerializer):
    scopes = ScopeSerializer(many=True, read_only=True)
    class Meta:
        model = Weapon
        fields = ['name','id','scopes']
