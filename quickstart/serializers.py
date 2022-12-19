from django.contrib.auth.models import User,Group
from rest_framework import serializers
from rest_framework import validators

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
        import pdb;pdb.set_trace()
        instance.name=validated_data.get('name',instance.name)
        instance.tagline=validated_data.get('tagline',instance.tagline)
        instance.save()
        return instance
  
    
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
    

class PublisherSeralizer(serializers.Serializer):
    name=serializers.CharField(max_length=100,required=False,allow_blank=True)
    publish_book=serializers.CharField(max_length=100,required=False,allow_blank=True)
    publish_date=serializers.CharField(max_length=100,required=False,allow_blank=True)
    comment_number=serializers.CharField(max_length=100,required=False,allow_blank=True)
    rating=serializers.CharField(max_length=100,required=False,allow_blank=True)
    
    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.publish_book=validated_data.get('publish_book',instance.publish_book)
        instance.publish_date=validated_data.get('publish_date',instance.publish_date)
        instance.comment_number=validated_data.get('comment_number',instance.comment_number)
        instance.rating=validated_data.get('rating',instance.rating)
        return instance
        
class ContactFormSeralizer(serializers.Serializer):
    name=serializers.CharField(max_length=100,allow_blank=False)
    age=serializers.IntegerField()
    email=serializers.EmailField(max_length=100,allow_blank=False)
    phone=serializers.IntegerField()
    
    def create(self, validated_data):
        return ContactForm.objects.create(**validated_data)
    
    def save(self):
        name=self.validated_data.get['name']
        age=self.validated_data.get['age']
        email=self.validated_data.get['email']
        phone=self.validated_data.get['phone']
               
class CollageSeralizer(serializers.Serializer):
    name=serializers.CharField(max_length=100,allow_blank=False,validators=["only collage name"])
    type_collage=serializers.CharField(max_length=100,allow_blank=False)
    location=serializers.CharField(max_length=100,allow_blank=False)
    pin_code=models.IntegerField()
    
    def create(self, validated_data):
        return Collage.objects.create(**validated_data)
    
    def update(self, request,instance, validated_data):
        # import pdb;pdb.set_trace()
        instance.name=validated_data.get('name',instance.name)
        instance.type_collage=validated_data.get('type_collage',instance.type_collage)
        instance.location=validated_data.get('location',instance.location)
        instance.pin_code=validated_data.get('pin_code',instance.pin_code)
        instance.save()
        return instance
    
    def save(self):
            name=self.validated_data.get['name']
            type_collage=self.validated_data.get['type_collage']
            location=self.validated_data.get['location']
            pin_code=self.validated_data.get['pin_code']
            
    def validate_value(self):
        if 'python' not in self.name.lower():
            raise serializers.ValidationError("blog post in not lower")
        return self.name
    
# class DepartmentSeralizer(serializers.ModelSerializer):
#     # collage_deparment_ser=CollageSeralizer(required=False)
#     collage_deparment_ser = serializers.IntegerField()
#     floor=serializers.IntegerField()
#     fields=serializers.CharField(max_length=100,allow_blank=True)
    
#     def validate(self, attrs):
#         import pdb;pdb.set_trace()
        
#         aa = super().validate(attrs)

#         return aa    
  
#     def create(self, validated_data):
#         # collage_deparment_ser=validated_data.pop('collage_deparment_ser')
#         # clg=Collage.objects.create(**validated_data)
        
#         dep=Department.objects.create(data='clg')
#         return dep
    
class PublisherSeralizer_1(serializers.ModelSerializer):
    
    class Meta:
        model=Publisher
        fields='__all__'
        depth=1
        read_only_field=['name']
        extra_kwargs={'pingback_rating':{'write_only':True}}
        
    def create(self,validated_data):
        pub=Publisher(
            name=self.validated_data.get['name'],
            publish_book=self.validated_data.get['publish_book'],
            publish_date=self.validated_data.get['publish_date'],
            comment_number=self.validated_data.get['comment_number'],
            rating=self.validated_data.get['rating']
            
        )
        pub.pingback_rating(validated_data['pingback_rating'])
        pub.save()
        return (pub)
    
class AlbumSerializer(serializers.Serializer):
    album_name=serializers.CharField(max_length=100,allow_blank=True)
    album_song=serializers.IntegerField()
    publish_date=serializers.DateField()
    update_date=serializers.DateField()
    
class AlbumSeralizer_1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Album
        fields='__all__'
        
class AlbumSerializer_2(serializers.HyperlinkedModelSerializer):
    
    url=serializers.HyperlinkedModelSerializer()
    class Meta:
        model=Album
        fields='__all__'
                
        
        