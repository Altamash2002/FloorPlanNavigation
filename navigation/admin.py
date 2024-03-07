from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Place)
admin.site.register(Teacher)
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Department)
admin.site.register(Visitor)