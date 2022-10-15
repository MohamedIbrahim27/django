from django.db import models

# Create your models here.
from django.db import models
from distutils.command.upload import upload
from django.utils.text import slugify

# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "project/%s.%s"%(instance.id,extension) 



def image_upload_detail1(instance,filename):
    imagename , extension = filename.split(".")
    return "project_detail/%s.%s"%(instance.id,extension) 
def image_upload_detail2(instance,filename):
    imagename , extension = filename.split(".")
    return "project_detail/%s.%s"%(instance.id,extension) 
def image_upload_detail3(instance,filename):
    imagename , extension = filename.split(".")
    return "project_detail/%s.%s"%(instance.id,extension) 
def image_upload_detail4(instance,filename):
    imagename , extension = filename.split(".")
    return "project_detail/%s.%s"%(instance.id,extension) 

class project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    category= models.ForeignKey('category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to =image_upload)
    
    ##  project information
    
    url_link = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to =image_upload_detail1 ,blank=True)
    image2 = models.ImageField(upload_to =image_upload_detail2,blank=True)
    image3 = models.ImageField(upload_to =image_upload_detail3,blank=True)
    image4 = models.ImageField(upload_to =image_upload_detail4,blank=True)
    slug = models.SlugField(blank=True ,null=True)
    
    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super(project,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title

class  category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name