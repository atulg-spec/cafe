from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import razorpay
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.shortcuts import render
import requests
from django import template
from cafe.settings import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
import qrcode
from io import BytesIO
from django.core.files import File
from googletrans import Translator
register = template.Library()

translator = Translator()


def lc(a):
    out = translator.translate(a,dest="hi")
    return out.text


def janm(request):
    if request.method == "POST":
        form = JanmForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = JanmForm()
    return render(request, 'janm.html',{'form':form,})

def aadhaar_form_view(request):
    if request.method == 'POST':
        form = AadhaarForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            f = Aadhaar.objects.get(id = f.id)
            link = f"Name:{f.name}, DOB: {f.date_of_birth}, Adhaar Number: {f.aadhaar_number}"
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            qr_code = code(adhaar = f)
            qr_code.qr.save(f'qr.png', File(buffer))
            qr_code.save()
            gender = ""
            if f.gender == "Male":
                gender = lc("Purush")
            else:
                gender = lc(f.gender)
            context = {"f":f,
                       "qr":qr_code,
                       "name":lc(f.name),
                       "gender":gender,
                       "address":lc(f.address),
                       }
            return redirect(f"adhar/{f.id}")
        else:
            print("Some error occured")
    else:
        form = AadhaarForm()
        form = AadhaarForm(initial={'user': request.user})  # Set the initial value for the user field
    # selected_language = request.GET.get('lang')
    # if selected_language:
    #     translation.activate(selected_language)
    #     request.session[translation.LANGUAGE_SESSION_KEY] = selected_language

        return render(request, 'adhar.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login') 
def home(request):
    adhar = Aadhaar.objects.filter(user=request.user)
    return render(request, 'index.html',{"adhar":adhar})

@login_required
def adhar(request,id):
    f = Aadhaar.objects.get(id=id)
    qr = code.objects.get(adhaar=f)
    return render(request,"addownload.html",{"f":f,"qr":qr})



def pan(request):
    if request.method == 'POST':
        form = PanCardForm(request.POST)
        if form.is_valid():
            pan_instance = form.save(commit=False)
            pan_instance.save()
            context = {
                'details': pan_instance.details,
                'form': form
            }
            return render(request, 'pan.html', context)
    else:
        form = PanCardForm()
    return render(request, 'pan.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_mobile = form.cleaned_data.get('email_or_mobile')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email_or_mobile, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def handlelogout(request):
    logout(request)
    return  redirect('/')


def contact(request):
    return render(request,"contact.html")