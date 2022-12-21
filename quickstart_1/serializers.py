from rest_framework import serializers
from quickstart_1.models import *
from rest_framework.serializers import ListSerializer

class UserSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,allow_blank=True)
    age=serializers.IntegerField()
    email=serializers.EmailField(max_length=100)
    phone=serializers.IntegerField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
       
class CompanySerializer(serializers.ModelSerializer):
    company_name=serializers.CharField(max_length=100,allow_blank=False)
    class Meta:
        model=Company
        fields='__all__'
        read_only_fields=['emp.name']
               
class UserSerializer_1(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','age','email']
        
class CompanySerializer_1(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields=['emp_name','emp_id','emp_email','emp_location','emp_phone']
        extra_kwargs={
            'url':{'view_name':'companyview','lookup_field':'id'}
        }
        
class CompanySerializer_2(serializers.ListSerializer):
    def create(self, validated_data):
        data=[Company(**item) for item in validated_data]
        return Company.objects.bulk_create(data)
    
class CompanySerializer_3(serializers.Serializer):
    emp_name=serializers.CharField(max_length=100,allow_blank=False)
    emp_id=serializers.IntegerField()
    emp_email=serializers.CharField(max_length=None,min_length=None,allow_blank=False)
    emp_location=serializers.CharField(max_length=50,min_length=None,allow_blank=False)
    emp_phone=serializers.IntegerField()
    
    class Meta:
        model=Company
        list_serializer_class=CompanySerializer_2

class HighscoreSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'player_name':instance.player_name,
            'score':instance.score
        }
        
class HighscoreSerializer_1(serializers.BaseSerializer):
    
    def to_internal_value(self, data):
        player_name=self.data.get('player_name')
        score=self.data.get('score')

        if not score:
            raise serializers.ValidationError('this field is required')
        if not player_name:
            raise serializers.ValidationError({'player_name':'this field in required'})
        if len(player_name)>10:
            raise serializers.ValidationError({'player_name':'your name may be only 10 character'})
        return {
            'player_name':player_name,
            'score':int(score)
        
        }
        
    def to_representation(self, instance):
        return {
            'player_name':instance.player_name,
            'score':instance.score
            }
        
    def create(self,instance,validated_data):
        instance.player_name=validated_data.get('player_name',instance.player_name)
        instance.score=validated_data.get('score',instance.score)
        instance.save()
        return HighScore(instance,**validated_data)
    
    def update(self,instance,validated_data):
        instance.player_name=validated_data.get('player_name',instance.player_name)
        instance.score=validated_data.get('score',instance.score)
        instance.save()
        return instance

class BasicSerializer(serializers.ModelSerializer):
    class Meta:
         model = HighScore
         fields = ('player_name','score')

class AdvandedSerializer(BasicSerializer):
    # import pdb;pdb.set_trace()
    additional_field = serializers.SerializerMethodField()

    def get_additional_field(self, obj):
        return('not important')

    class Meta(BasicSerializer.Meta):
        fields = BasicSerializer.Meta.fields + ('additional_field',)
        
class HospitalSerializer(serializers.Serializer):
    hos_name=serializers.CharField(max_length=100,write_only=True)
    hos_type=serializers.CharField(max_length=100,required=True,)
    hos_location=serializers.CharField(max_length=100,allow_null=True,required=True,write_only=True)
    hos_department=serializers.CharField(source='department')  
    

# class UserSerializer(serializers.Serializer):
#     url = serializers.URLField(max_length=255,min_length=None,allow_blank=False)
#     first_name = serializers.ListField(max_length=255,min_length=None,allow_blank=True)
#     last_name = serializers.DictField(max_length=255,min_length=None,allow_blank=True)
#     email = serializers.EmailField(max_length=255,min_length=None,allow_blank=False)
#     address = serializers.CharField(max_length=100,min_length=None,allow_blank=False)
#     phone = serializers.DictField()
#     messenger_id = models.IntegerField(max_value=100,min_value=None,allow_blank=False)

class HospitalSerializer_1(serializers.ModelSerializer):
    hospital_1=serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Hospital_1
        fields=['hos_id','hos_name','hos_address','hos_city','hospital_1']
        
class HospitalSerializer_2(serializers.ModelSerializer):
    hospital_1=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Hospital_1
        fields='__all__'
        
class PatientSerializer_1(serializers.ModelSerializer):
    # performaning actions
    patient=serializers.StringRelatedField(many=True)
    class Meta:
        model=Patient
        fields='__all__'
        
class PatientSerializer_2(serializers.ModelSerializer):
    patient=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    
    class Meta:
        model=Patient
        fields='__all__'
        
        

    
 