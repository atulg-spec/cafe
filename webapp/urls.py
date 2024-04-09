from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path("logout",handlelogout,name='logout'),
    path('', home, name='home'),
    path('pan', pan, name='pan'),
    path('adf', aadhaar_form_view, name='aadhaar_form'),
    path('jn', janm, name='janm'),
    path('contact', contact, name='contact'),
    path('adhar/<str:id>', adhar, name='adhar'),
]
