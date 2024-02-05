from django.contrib import admin
from core.admin import *
from core.models import *

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Note)