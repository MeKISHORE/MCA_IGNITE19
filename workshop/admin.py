from django.contrib import admin
from .models import collegeverification, contact_us, studentregistration

admin.site.register(studentregistration)
admin.site.register(collegeverification)
admin.site.register(contact_us)
