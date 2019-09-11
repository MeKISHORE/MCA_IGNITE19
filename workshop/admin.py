from django.contrib import admin
from .models import collegeverification, contact_us, studentregistration,events,event_details

admin.site.register(studentregistration)
admin.site.register(collegeverification)
admin.site.register(contact_us)
admin.site.register(events)
admin.site.register(event_details)

