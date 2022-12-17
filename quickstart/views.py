from rest_framework import serializers
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import *
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.throttling import UserRateThrottle
from rest_framework.schemas import AutoSchema
from rest_framework.permissions import *
from rest_framework import generics
from django.db.models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import BaseFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import *
from rest_framework.authentication import *
from rest_framework.routers import Route,DynamicRoute,SimpleRouter
from rest_framework.parsers import *
import io
from rest_framework.parsers import JSONParser
@csrf_exempt
@api_view(['GET','POST'])
def entryseralizer(request):
    if request.method=='GET':
        entry=Entry.objects.all()
        seralizer=EntrySerializer(entry,many=True)
        seralizer_1=seralizer.data
        return Response(seralizer_1,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        # import pdb;pdb.set_trace()
        data=JSONParser().parse(request)
        seralizer=EntrySerializer(data=data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data,status=status.HTTP_200_OK)
        return Response(seralizer,status=status.HTTP_400_BAD_REQUEST)
    
    
class EntryListView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    renderer_classes=[JSONRenderer]

    
    def get(self,request,*args,**kwargs):
        
        user=[user.username for user in User.objects.all()]
        return Response(user) 

@api_view()
def fun_1(request):
    return Response({"message":"hello_world"})

@api_view(['POST'])
def hello_world(request):
    if request.method=='POST':
        return Response({"message":"Get some data","data":request.data})
    return Response({"message":"hello world"})

class OncePerDayUserThrottle(UserRateThrottle):
    rate='1\day'
@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def view(request):
    return Response({'message':"hello_world"})

class CustomAutoScehma(AutoSchema):
    
    def get_link(self, path, method, base_url):
        return super().get_link(path, method, base_url)
    
@api_view(['GET'])
@schema([CustomAutoScehma])
def customschema(request):
    return Response({"message":"Done"})


class EntryList(generics.ListAPIView):
    queryset=Entry.objects.all().annotate(Count('number_comment'))
    serializer_class=EntrySerializer
    permission_classes=[IsAdminUser]

    def list(self,request):
        # import pdb;pdb.set_trace()
        queryset=self.get_queryset()
        serializer=EntrySerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
class EntryDetail(generics.RetrieveAPIView):
    queryset=Entry.objects.filter().all().values()
    serializer_class=EntrySerializer
    permission_classes=[IsAdminUser]
    pagination_class=[PageNumberPagination]
    filter_backends=[BaseFilterBackend]
        
    def detail(self,request):
        query_set=self.get_queryset()
        serializer=self.get_serializer_class(query_set)
        permission=self.get_permissions(IsAuthenticatedOrReadOnly)
        pagination=self.get_paginated_response(PageNumberPagination)
        return Response(serializer.data,permission,pagination,status=status.HTTP_200_OK)
    
class BlogList(generics.ListAPIView):
    serializer_class=BlogSerializer
    
    def get_queryset(self):
        
        return Blog.objects.filter().annotate(Count('name'))
    
    def get_object(self):
        # import pdb;pdb.set_trace()
        queryset=self.get_queryset()
        filter={}
        for field in self.multiple_lookups_fields:
            filter[field]=self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        return obj
    
    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
    
    def get_serializer_class(self):
        # import pdb;pdb.set_trace()
        queryset=self.get_queryset()
        if queryset.filter(name='this is python blog'):
            return BlogSerializer
        else:
            raise AttributeError("this is else part")
        
        
class BlogView(generics.GenericAPIView,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               ):
    
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class BlogView_1(generics.GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin
                 ):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class AuthorView(generics.CreateAPIView,
                 generics.RetrieveAPIView,
                 generics.UpdateAPIView
                 ):
    queryset=Author.objects.all()
    serializer_class=AuthorSeralizer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.update(request,*args,**kwargs)
    
class AuthorView_1(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.filter().annotate(Count('name'))
    serializer_class=AuthorSeralizer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class EntryViewSet(viewsets.ViewSet):
    
    def list(self,request):
        sni=Entry.objects.all()
        seralizer=EntrySerializer(sni,many=True)
        seralizer_1=seralizer.data
        return Response(seralizer_1,status=status.HTTP_200_OK)
    
    def retrive(self,request,pk=None):
        queryset=Entry.objects.all()
        obj=get_object_or_404(queryset,pk=pk)
        serializer=EntrySerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class EntryViewSet_1(viewsets.ModelViewSet):
    queryset=Entry.objects.all()
    serializer_class=EntrySerializer
    
class ItemsList(APIView):
    
    parser_classes=[FormParser]
    def get(self,request,*args,**kwargs):

        aut=Author.objects.all()
        serializer=AuthorSeralizer(aut,many=True)
        serializer_1=serializer.data
        return Response(serializer_1,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwrags):
        serializer_data=AuthorSeralizer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class ItemsDetail(APIView):
    
    parser_classes=[]
    
    def get(self,request,pk,*args,**kwargs):
        blog=get_object_or_404(Blog.objects.all(),pk=pk)
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,*args,**kwrags):
        data=get_object_or_404(Blog.objects.all(),pk=pk)
        serializer_data=BlogSerializer(data,request.data) 
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,*args,**kwargs):
        data=get_object_or_404(Blog.objects.all(),pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
    
class EntryViewSet(viewsets.ModelViewSet):
    queryset=Entry.objects.all()
    serializer_class=EntrySerializer
    # permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Entry.objects.all()
    
class AuthorViewSet(viewsets.ViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSeralizer
    # permission_classes=[IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Author.objects.all()
    
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='name'
    
    def tagline_name(self,request,*args,**kwrags):
        blog=self.get_object
        blog_1=blog.name.all()
        return Response([blog.name for group in blog_1])

    
class ExampleView(APIView):
    # queryset=Blog.objects.all()
    # serializer=BlogSerializer
    parser_classes=[JSONParser] 
    
    def get(self,request,*args,**kwrags):
        sni=Blog.objects.all()
        serializer=BlogSerializer(sni,many=True)
        serializer_1=serializer.data
        return Response(serializer_1,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        seralizer=BlogSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class ItemsList(APIView):
    def get(self,request,*args,**kwargs):

        aut=Author.objects.all()
        serializer=AuthorSeralizer(aut,many=True)
        serializer_1=serializer.data
        return Response(serializer_1,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwrags):
        serializer_data=AuthorSeralizer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class ItemsViewset(viewsets.ViewSet):
    
    def list(self,request,*args,**kwargs):

        aut=Author.objects.all()
        serializer=AuthorSeralizer(aut,many=True)
        serializer_1=serializer.data
        return Response(serializer_1,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwrags):
        serializer_data=AuthorSeralizer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class ItemsViewset1(viewsets.ViewSet):
    # import pdb;pdb.set_trace()
    def list(self,request,pk,*args,**kwargs):
        blog=get_object_or_404(Blog.objects.all(),pk=pk)
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk,*args,**kwrags):
        data=get_object_or_404(Blog.objects.all(),pk=pk)
        serializer_data=BlogSerializer(data,request.data) 
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk,*args,**kwargs):
        data=get_object_or_404(Blog.objects.all(),pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DemoView(APIView):
    parser_classes=[JSONParser]
    # permission_classes=[IsAuthenticated]
    
    def get(self,request,*args,**kwrags):
        sni=Blog.objects.all()
        serializer=BlogSerializer(sni,many=True)
        serializer_1=serializer.data
        return Response(serializer_1,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwrags):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class DemoView_1(APIView):
    parser_classes=[JSONParser]
    
    def get(self,request,pk,*args,**kwargs):
        blog=get_object_or_404(Blog.objects.all(),pk=pk)
        serializer=BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,*args,**kwrags):
        # import pdb;pdb.set_trace()
        data=get_object_or_404(Blog.objects.all(),pk=pk)
        serializer_data=BlogSerializer(data,request.data) 
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk,*args,**kwargs):
        data=get_object_or_404(Blog.objects.all(),pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PublisherView(APIView):
    def get(self,request,*args,**kwargs):
        serializer=PublisherSeralizer()
        seralizer_1=serializer.data
        print(seralizer_1)
        json=JSONRenderer().render(seralizer_1)
        print(json)
        stream=io.BytesIO(json)
        json_parser=JSONParser().parse(stream)
        print(json_parser)
        serializer=PublisherSeralizer(data=json_parser)
        a=serializer.is_valid()
        print(a)
        print(serializer.validated_data)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        serializer=PublisherSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ContactFormView(APIView):
    
    def get(self,request,*args,**kwargs):
        sni=ContactForm.objects.all()
        serializer=ContactFormSeralizer(sni,many=True)
        ser=serializer.data
        return Response(ser,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        # import pdb;pdb.set_trace()
        serializer=ContactFormSeralizer(ContactForm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            serializer.errors
            
            
            
    
        
        

        
    
        
    
      
        
    
    

           

    

   
    
        
    

    
    

    
    
    
    
    

    
    