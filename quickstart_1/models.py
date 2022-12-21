from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.PositiveIntegerField()
    email=models.EmailField(max_length=100,help_text='@gmail.com')
    phone=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    emp_name=models.CharField(max_length=100,null=True,blank=True)
    emp_id=models.BigIntegerField()
    emp_email=models.EmailField(max_length=100)
    emp_location=models.CharField(max_length=100,null=True,blank=True)
    emp_phone=models.IntegerField()
    
class HighScore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    player_name = models.CharField(max_length=10)
    score = models.IntegerField()
    
class Hospital(models.Model):
    hos_name=models.CharField(max_length=100,null=True,blank=True)
    hos_type=models.CharField(max_length=100,null=True,blank=True)
    hos_location=models.CharField(max_length=100,null=True,blank=True)
    hos_department=models.CharField(max_length=100,null=True,blank=True)
    
class User_1(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    messenger_id = models.IntegerField()
    
class Hospital_1(models.Model):
    hos_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    hos_name=models.CharField(max_length=100,null=True,blank=True)
    hos_address=models.CharField(max_length=100,null=False,blank=False)
    hos_city=models.CharField(max_length=100,null=False,blank=False)
         
    def __str__(self):
        return self.hos_name
    
class Patient(models.Model):
    hos_p=models.ForeignKey(Hospital_1,on_delete=models.CASCADE,related_name='hospital_1',null=True,blank=True)
    p_name=models.CharField(max_length=100,null=False,blank=False)
    p_diagnosis=models.CharField(max_length=100,null=True,blank=True)
    p_address=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.p_name
    
class Medical_Record(models.Model):
    med_p=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='patient',null=True,blank=True)
    date_of_examination=models.DateTimeField(auto_now_add=True)
    patient_problem=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.patient_problem
    
class Doctor(models.Model):
    hos_doc=models.ForeignKey(Hospital_1,on_delete=models.CASCADE,related_name='doc_hospital',null=True,blank=True)
    doc_name=models.CharField(max_length=100,null=True,blank=True)
    doc_qualification=models.CharField(max_length=100,null=True,blank=True)
    doc_salary=models.IntegerField()
    
    def __str__(self):
        return self.doc_name
    
    
    
    
    
    
    
    
       