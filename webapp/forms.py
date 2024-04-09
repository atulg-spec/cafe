from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
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

class JanmForm(forms.ModelForm):
    class Meta:
        model = Janm
        fields = "__all__"
        widgets={
            "name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "aadhaar_number":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "gender":forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "date_of_birth":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "date_of_birth_in_words":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "place_of_birth":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "place_of_birth_local":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "father_name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "father_aadhaar_number":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "mother_name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "mother_aadhaar_number":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "permanent_address":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "birth_address":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "local_language":forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "date_of_registration":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "date_of_issue":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "state":forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "hospital_name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
        }

    # name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # aadhaar_number = forms.CharField(label='आधार नंबर / Aadhaar Number', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # gender = forms.ChoiceField(label='Select Gender', choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # date_of_birth = forms.DateField(label='जन्म तिथि / Date Of Birth', widget=forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # date_of_birth_in_words = forms.CharField(label='जन्म तिथि / Date Of Birth ( IN WORDS )', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # place_of_birth = forms.CharField(label='Place Of Birth', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # place_of_birth_local = forms.CharField(label='Place Of Birth (Local Language)', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # father_name = forms.CharField(label='NAME OF FATHER', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # father_aadhaar_number = forms.CharField(label="पिता का आधार / Father's Aadhaar No.", widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # mother_name = forms.CharField(label='NAME OF MOTHER', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # mother_aadhaar_number = forms.CharField(label="Mother's Aadhaar No.", widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # permanent_address = forms.CharField(label='Permanent Address', widget=forms.Textarea(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # birth_address = forms.CharField(label='Address at the time of Birth', widget=forms.Textarea(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # local_language = forms.ChoiceField(label='Select Local Language', choices=LOCAL_LANGUAGE_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # date_of_registration = forms.DateField(label='Date Of Registration', widget=forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # date_of_issue = forms.DateField(label='Date Of Issue', widget=forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # state = forms.ChoiceField(label='Select State', choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # hospital_name = forms.CharField(label='Select Hospital', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))

class AadhaarForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Aadhaar
        fields = "__all__"
        widgets={
            "aadhaar_number":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "gender":forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "date_of_birth":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "relation":forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "father_husband_name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "house_number":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "street":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "area":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "district":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "state":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "pin_code":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "address":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "photo":forms.ClearableFileInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "local_language":forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "local_name":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "local_address":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "enrollment_number":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "issue_date":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
            "download_date":forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'})
        }
    # aadhaar_number = forms.CharField(label='Aadhaar Number', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # gender = forms.ChoiceField(label='Select Gender', choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # date_of_birth = forms.DateField(label='Date of Birth (DD/MM/YYYY)', input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # relation = forms.ChoiceField(label='Relation', choices=RELATION_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # father_husband_name = forms.CharField(label='Father/Husband Name', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # house_number = forms.CharField(label='House No./Ward No./Building/Apartment', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # street = forms.CharField(label='Street/Road/Lane', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # area = forms.CharField(label='Area/Locality/Village/Nearby', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # district = forms.CharField(label='District', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # pin_code = forms.CharField(label='Pin Code', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500', 'rows': 3}))
    # photo = forms.ImageField(label='Upload Photo', widget=forms.ClearableFileInput(attrs={'class': 'border border-gray-300 py-2 px-4 focus:outline-none focus:ring focus:border-blue-500'}))
    # local_language = forms.ChoiceField(label='Select Local Language', choices=LOCAL_LANGUAGE_CHOICES, widget=forms.Select(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # local_name = forms.CharField(label='Name (Local Language)', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # local_address = forms.CharField(label='Address (Local Language)', widget=forms.Textarea(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500', 'rows': 3}))
    # enrollment_number = forms.CharField(label='Enrollment No. (Optional)', required=False, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # issue_date = forms.DateField(label='Issue Date (DD/MM/YYYY) (Optional)', input_formats=['%d/%m/%Y'], required=False, widget=forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    # download_date = forms.DateField(label='Download Date (DD/MM/YYYY) (Optional)', input_formats=['%d/%m/%Y'], required=False, widget=forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    mobile_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'})
        self.fields['last_name'].widget.attrs.update({'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'})
        self.fields['password1'].widget.attrs.update({'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'})
        self.fields['password2'].widget.attrs.update({'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # messages.success(request, 'Registration successful.')
        return user




class LoginForm(forms.Form):
    email_or_mobile = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}))


# PAN FORM 
class PanCardForm(forms.ModelForm):
    class Meta:
        model = pan_card
        fields = ['pan_no']
        widgets = {
            'pan_no': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-4 w-full focus:outline-none focus:ring focus:border-blue-500'}),
        }
