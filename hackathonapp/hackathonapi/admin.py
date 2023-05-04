from django.contrib import admin
from .models import Hackathon,ParticipantRegistration,Submission
# Register your models here.
admin.site.register(Hackathon)
admin.site.register(ParticipantRegistration)
admin.site.register(Submission)
