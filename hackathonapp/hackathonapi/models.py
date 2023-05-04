from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
#from django.contrib.sites.models import Site
class Hackathon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon/images/')
    hackathon_image = models.ImageField(upload_to='hackathon/images/')
    SUBMISSION_TYPE_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    submission_type = models.CharField(max_length=10, choices=SUBMISSION_TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    participants = models.ManyToManyField(User, related_name='enrolled_hackathons', blank=True)

    def __str__(self):
        return self.title

class ParticipantRegistration(models.Model):
    participant_name = models.CharField(max_length=255)
    email = models.EmailField()
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='registrations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.participant_name

    class Meta:
        verbose_name = _('Participant Registration')
        verbose_name_plural = _('Participant Registrations')
        unique_together = ('email', 'hackathon')

class Submission(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_image = models.ImageField(upload_to='submission/images/', null=True, blank=True)
    submission_file = models.FileField(upload_to='submission/files/', null=True, blank=True)
    submission_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

       


#hackathon = Hackathon(title="My Hackathon", description="...", background_image="",hackathon_image="",submission_type= "file", start_datetime="2023-06-01", end_datetime="2023-06-02",reward_prize="100" ,created_by_id=1)
#hackathon.save()


