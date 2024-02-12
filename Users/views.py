from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import FleetManagers,Fleets
from .serializers import RegisterFleetManagerSerializer,RegisterFleetSerializer,LoginFleetManagerSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login


# Create your views here.


class FleetManagerRegistration(viewsets.ModelViewSet):
    queryset=FleetManagers.objects.all()
    serializer_class=RegisterFleetManagerSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data 
        serializer = RegisterFleetManagerSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Message": "Registration Successful", "token": str(token)}, status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response({"Message": "Registration not Successful"}, status.HTTP_400_BAD_REQUEST)



class CustomUserAuthentication(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = FleetManagers.objects.get(username=username)
            if user.check_password(password):
                return user
        except FleetManagers.DoesNotExist:
            return None
        

class FleetManagerLogin(viewsets.ModelViewSet):
    queryset=FleetManagers.objects.all()
    serializer_class=LoginFleetManagerSerializer
    http_method_names=['post']

    def create(self,request):
        data=request.data
        serializer=LoginFleetManagerSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            },status.HTTP_400_BAD_REQUEST)

        user = CustomUserAuthentication().authenticate(request, username=serializer.data['username'], password=serializer.data['password'])
        if not user:
            return Response({
                'status':False,
                'message':'Invalid Credentials'
            },status.HTTP_400_BAD_REQUEST)
        token, _= Token.objects.get_or_create(user=user)
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')

        return Response({'status':True,'message':'user login','user':str(user.first_name)+" "+str(user.last_name),'token':str(token)},status.HTTP_201_CREATED)


class FleetRegistration(viewsets.ModelViewSet):
    queryset=Fleets.objects.all()
    serializer_class=RegisterFleetSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data 
        companyName=data.get('companyName')
        data['companyName']=FleetManagers.objects.get(CompanyName=data['companyName']).id
        print(data)
        serializer = RegisterFleetSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            # token, created = Token.objects.get_or_create(user=user)
            return Response({"Message": "Registration Successful"}, status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response({"Message": "Registration not Successful"}, status.HTTP_400_BAD_REQUEST)