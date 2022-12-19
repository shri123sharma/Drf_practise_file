from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class User_1(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    
class Snippet(models.Model):
    owner=models.ForeignKey(User_1,related_name='user_owner',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    highlighted=models.CharField(max_length=100,null=True,blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    langauage = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
        
class Blog(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    tagline=models.TextField()
    
    def __str__(self):
        return self.name 
    
class Author(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
   
class Entry(models.Model):
    headline=models.CharField(max_length=100)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    number_comment=models.IntegerField()
    number_pingback=models.IntegerField()
    rating=models.IntegerField(default=5)
    
    
class Publisher(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    publish_book=models.CharField(max_length=100,null=True,blank=True)
    publish_date=models.CharField(max_length=100,null=True,blank=True)
    comment_number=models.CharField(max_length=100,null=True,blank=True)
    rating=models.CharField(max_length=100,null=True,blank=True)
    
class ContactForm(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField()
    email=models.EmailField(max_length=100,help_text='only for email',default='@gmail.com')
    phone=models.IntegerField()
    
    
class Collage(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    type_collage=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    pin_code=models.IntegerField()
    
    def __str__(self):
        return self.name

class Department(models.Model):
    collage_department=models.ForeignKey(Collage,on_delete=models.CASCADE,null=True,blank=True)
    floor=models.IntegerField(null=False,blank=False)
    fields=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.floor)
    
class Section(models.Model):
    dep_section=models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE)
    classes=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.dep_section)
    
class Album(models.Model):
    
    album_name=models.CharField(max_length=100,null=True,blank=True)
    album_song=models.IntegerField()
    publish_date=models.DateField(auto_now_add=True)
    update_date=models.DateField()
    
    
