from rest_framework import serializers

from .models import FleetManagers,Fleets

class RegisterFleetManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FleetManagers
        fields = ["first_name", "last_name", "username", "email", "password", "CompanyName"]


    def validate(self, data):
        if data['username']:
            if FleetManagers.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username is taken')
        return data
    
    def create(self, validated_data):
        user=FleetManagers.objects.create(username=validated_data['username'],email=validated_data['email'],
                    last_name=validated_data['last_name'],first_name=validated_data['first_name'],CompanyName=validated_data['CompanyName'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginFleetManagerSerializer(serializers.Serializer):
    username= serializers.CharField()
    password=serializers.CharField()


class RegisterFleetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Fleets
        fields='__all__'

    def validate(self, data):
        if data['license_no']:
            if Fleets.objects.filter(license_no=data['license_no']).exists():
                raise serializers.ValidationError('license no already exists.')
        if data['hardware_id']:
            if Fleets.objects.filter(hardware_id=data['hardware_id']).exists():
                raise serializers.ValidationError('hardware_id already exists.')
        return data