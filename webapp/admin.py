from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Janm)
admin.site.register(Aadhaar)
admin.site.register(pan_card)

admin.site.unregister(Group)
admin.site.site_title = "Aadhaar"
admin.site.site_header = "Dashboard"
admin.site.index_title = "Aadhaar Dashboard"