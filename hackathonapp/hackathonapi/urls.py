from django.urls import path,include
from . import views
from django.conf import settings
from .views import HackathonListCreate,HackathonList,SubmissionListCreate,ParticipantRegistrationViewSet,EnrolledHackathonListView,UserHackathonSubmissionListView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hackathons/(?P<hackathon_id>\d+)/registrations', ParticipantRegistrationViewSet, basename='registration')

urlpatterns = [
    path('',HackathonList.as_view(), name='hackathon_list'),
    path('create-hackathons/',HackathonListCreate.as_view()),
    path('submissions/', SubmissionListCreate.as_view()),
    path('', include(router.urls)),
    path('enrolled-hackathons/', EnrolledHackathonListView.as_view(), name='enrolled_hackathons'),
    path('hackathons/<int:hackathon_id>/submissions/', UserHackathonSubmissionListView.as_view(), name='user_hackathon_submissions'),
]
