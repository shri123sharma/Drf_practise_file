from django.shortcuts import render
from quickstart_1.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from json import loads,dumps
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view


class UserSerailazerView(APIView):
    
    def get(self,request,*args,**kwargs):
        user=User.objects.all()
        ser=UserSerializer(user,many=True)
        serializer=ser.data
        return Response(serializer,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserSerializerView_1(APIView):
    def get(self,request):   
        user_1=User.objects.all()
        ser=UserSerializer_1(user_1,many=True)
        serializer=ser.data
        return Response(serializer,status=status.HTTP_200_OK)
    
class CompanySerializerView(APIView):
    def get(self,request):
        comp_1=Company.objects.all()
        comp_ser=CompanySerializer_3(comp_1,many=True,context={'request': request})
        print(repr(comp_ser))
        serializer=comp_ser.data
        return Response(serializer,status=status.HTTP_200_OK)
 
@api_view(['GET'])   
def highscore_view(request,*args,**kwargs):
        queryset=HighScore.objects.all()
        ser=HighscoreSerializer(queryset,many=True)
        serializer=ser.data
        return Response(serializer,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def highscore_view_1(request,pk,*args,**kwargs):
    queryset_1=HighScore.objects.get(pk=pk)
    ser=HighscoreSerializer(queryset_1)
    serializer=ser.data
    return Response(serializer,status=status.HTTP_200_OK)

@api_view(['GET'])
def highscore_represent(request,*args,**kwrags):
    queryset_2=HighScore.objects.all()
    ser=HighscoreSerializer_1(queryset_2,many=True)
    serializer=ser.data
    return Response(serializer,status=status.HTTP_200_OK)

class HighScoreSerializerView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=HighScore.objects.all()
        ser=AdvandedSerializer(queryset,many=True)
        serializer=ser.data
        return Response(serializer,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        ser_1=HighscoreSerializer_1(data=request.data,many=True)
        if ser_1.is_valid():
            ser_1.save()
            return JsonResponse(ser_1.data,status=status.HTTP_201_CREATED)
        else:
            raise serializers.ValidationError('Bad Request 404')
        
class HospitalSerializerView(APIView):
    def get(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        hos=Hospital.objects.all()
        serializer=HospitalSerializer(hos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def hospital_1(request,*args,**kwargs):
    queryset=Hospital_1.objects.all()
    ser=HospitalSerializer_1(queryset,many=True)
    print(repr(ser))
    serializer=ser.data
    return Response(serializer,status=status.HTTP_200_OK)

@api_view(['GET'])
def patient_1(request,*args,**kwargs):
    queryset=Patient.objects.all()
    ser=PatientSerializer_2(queryset,many=True)
    print(repr(ser))
    serializer=ser.data
    return Response(serializer,status=status.HTTP_200_OK)

    
             

