from django.contrib.auth.models import User,Group
from rest_framework import serializers

from .models import *

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=User
#         fields=['url','username','email','groups']
        
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Group
#         fields=['url','name']
    
    
#     def update(self, instance, validated_data):
#         instance.title=validated_data.get('title',instance.title)
#         instance.code=validated_data.get('code',instance.code)
#         instance.linenos=validated_data.get('title',instance.linenos)
#         instance.langauage=validated_data.get('langauage',instance.langauage)
#         instance.style=validated_data.get('style',instance.style)
#         instance.save()
#         return instance
#         # return super().update(instance, validated_data)
        
# class SnippetSerializer_1(serializers.ModelSerializer):
#     class Meta:
#         model=Snippet
#         fields=['id','title','code','langauage','linenos']
        
# class BlogSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100,required=False,allow_blank=True)
#     tagline=serializers.CharField(max_length=100,required=False,allow_blank=True)
    
#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)
    
# class BlogSerializer_1(serializers.ModelSerializer):
#     class Meta:
#         model=Blog
#         fields=['id','name','tagline']
        
#         def create(self, validated_data):
#             return self.Blog.objects.create(validated_data)
        
# class UserSerializer(serializers.ModelSerializer):
#     # user_owner_serializer=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
#     class Meta:
#         model=User
#         fields=['id','username','password','user_owner_serializer']\
    

# class UserSerializer_1(serializers.ModelSerializer):
    
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']
        
class SnippetSerializer(serializers.Serializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(required=False,allow_blank=True,max_length=100)
    highlighted=serializers.ReadOnlyField()
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
    
    def create(self, validated_data):
        return Snippet.objects.create(validated_data)
    
class EntrySerializer(serializers.Serializer):
    headline=serializers.CharField(required=False,allow_blank=True,max_length=100)
    body_text=serializers.ReadOnlyField()
    pub_date=serializers.DateField()
    mod_date=serializers.DateField()
    number_comment=serializers.IntegerField()
    number_pingback=serializers.IntegerField()
    rating=serializers.IntegerField()
    
    def create(self, validated_data):
        return Entry.objects.create(**validated_data)
    
class BlogSerializer(serializers.Serializer):
    name=serializers.CharField(required=False,allow_blank=True,max_length=100)
    tagline=serializers.CharField(required=False,allow_blank=True,max_length=100)
    
    def create(self,validated_data):
        return Blog.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        # import pdb;pdb.set_trace()
        instance.name=validated_data.get('name',instance.name)
        instance.tagline=validated_data.get('tagline',instance.tagline)
        instance.save()
        return instance
        # return super().update(instance, validated_data)     
    
class AuthorSeralizer(serializers.Serializer):
    name=serializers.CharField(required=False,allow_blank=True,max_length=100)
    email=serializers.CharField(required=False,allow_blank=True,max_length=100)
    
    def create(self,validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self,pk,instance,validated_data):
        
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance
    
    def delete(self,pk,validated_data):
        data=Author.objects.get(id=pk).delete()
        return data
    

                
    
    
    


    
    
    
        





    

