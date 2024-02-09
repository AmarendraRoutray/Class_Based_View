from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Songs)
admin.site.register(Whisky)

admin.site.register(School)
admin.site.register(Student)