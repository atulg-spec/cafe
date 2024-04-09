from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
import requests

User = get_user_model()

class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)
    email_verification_otp = models.CharField(max_length=6, blank=True, null=True)
    
    # Adding related_name to resolve clashes
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username
    

GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

RELATION_CHOICES = [
        ('Father', 'Father'),
        ('Husband', 'Husband')
    ]

LOCAL_LANGUAGE_CHOICES = [
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Telugu', 'Telugu')
    ]

STATE_CHOICES = [
    ('state1', 'State 1'),
    ('state2', 'State 2'),
    ('state3', 'State 3'),
]

class Janm(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    aadhaar_number = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES,default="Male")
    date_of_birth = models.CharField(max_length=100,null=True)
    date_of_birth_in_words = models.CharField(max_length=100,null=True)
    place_of_birth = models.CharField(max_length=100,null=True)
    place_of_birth_local = models.CharField(max_length=100,null=True)
    father_name = models.CharField(max_length=100,null=True)
    father_aadhaar_number = models.CharField(max_length=100,null=True)
    mother_name = models.CharField(max_length=100,null=True)
    mother_aadhaar_number = models.CharField(max_length=100,null=True)
    permanent_address = models.CharField(max_length=100,null=True)
    birth_address = models.CharField(max_length=100,null=True)
    local_language = models.CharField(max_length=50,choices=LOCAL_LANGUAGE_CHOICES,default="English")
    date_of_registration = models.CharField(max_length=100,null=True)
    date_of_issue = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,choices=STATE_CHOICES,default="state1")
    hospital_name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
    

class Aadhaar(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=True)
    aadhaar_number = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    photo=models.ImageField(upload_to="photo",null=True)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES,default="Male")
    date_of_birth = models.CharField(max_length=50,default="")
    relation = models.CharField(max_length=50,choices=RELATION_CHOICES,default="Father")
    father_husband_name = models.CharField(max_length=100,null=True)
    house_number = models.CharField(max_length=100,null=True)
    street = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    pin_code = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    local_language = models.CharField(max_length=50,choices=LOCAL_LANGUAGE_CHOICES,default="English")
    local_name = models.CharField(max_length=100,null=True)
    local_address = models.CharField(max_length=100,null=True)
    enrollment_number = models.CharField(max_length=100,null=True,blank=True)
    issue_date = models.CharField(max_length=50,null=True,blank=True,default="")
    download_date = models.CharField(max_length=50,null=True,blank=True,default="")
    def __str__(self):
        return self.name
    
class code(models.Model):
    adhaar = models.ForeignKey(Aadhaar,on_delete=models.CASCADE)
    qr=models.ImageField(upload_to="qr",null=True)


class pan_card(models.Model):
    pan_no = models.CharField(max_length=100,null=True)
    response = models.BooleanField(default=True)
    details = models.TextField()
    def __str__(self):
        return self.pan_no
    def save(self, *args, **kwargs):
        url = "https://pan-information-verification-api.p.rapidapi.com/validation/api/v1/panverification"

        payload = {
        	"pan": self.pan_no,
        	"consent": "yes",
        	"consent_text": "I hear by declare my consent agreement for fetching my information via AITAN Labs API"
        }
        headers = {
        	"content-type": "application/json",
        	"X-RapidAPI-Key": "4dc314e637msh5ce7226f78fa04ep1d1e71jsn1464d9d07898",
        	"X-RapidAPI-Host": "pan-information-verification-api.p.rapidapi.com"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        self.details = response.json()
        try:
            if not response.json()['status'] == 'success':
                self.response = False
            print(response.json())
        except:
            self.details = response.json()
        super().save(*args, **kwargs)    
