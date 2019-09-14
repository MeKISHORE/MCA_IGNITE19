from django.contrib import admin
from .models import collegeverification, contact_us, studentregistration,events,event_details,teams,team_images

admin.site.register(studentregistration)
admin.site.register(collegeverification)
admin.site.register(contact_us)
admin.site.register(events)
admin.site.register(event_details)
admin.site.register(teams)
admin.site.register(team_images)


