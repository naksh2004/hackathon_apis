from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,permissions
from .models import Hackathon,ParticipantRegistration,Submission
from .serializer import HackathonSerializer,SubmissionSerializer,ParticipantRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action

class HackathonList(generics.ListAPIView):
    serializer_class = HackathonSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Hackathon.objects.all()

class HackathonListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HackathonSerializer

    def get_queryset(self):
        return Hackathon.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SubmissionListCreate(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Submission.objects.filter(user=self.request.user)
        hackathon_id = self.request.query_params.get('hackathon_id', None)
        if hackathon_id is not None:
            queryset = queryset.filter(hackathon_id=hackathon_id)
        return queryset

    def perform_create(self, serializer):
        hackathon_id = self.request.data['hackathon']
        hackathon = Hackathon.objects.get(id=hackathon_id)
        submission_type = hackathon.submission_type

        if submission_type == 'image':
            image = self.request.data['submission_image']
            serializer.save(user=self.request.user, hackathon=hackathon, submission_image=image)
        elif submission_type == 'file':
            file = self.request.data['submission_file']
            serializer.save(user=self.request.user, hackathon=hackathon, submission_file=file)
        elif submission_type == 'link':
            link = self.request.data['submission_link']
            serializer.save(user=self.request.user, hackathon=hackathon, submission_link=link)
        else:
            raise serializers.ValidationError('Invalid submission type.')




class ParticipantRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ParticipantRegistration.objects.all()
    serializer_class = ParticipantRegistrationSerializer

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        hackathon = self.get_object()
        data = request.data
        data['hackathon'] = hackathon.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
class EnrolledHackathonListView(generics.ListAPIView):
    serializer_class = HackathonSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        participant_registrations = ParticipantRegistration.objects.filter(email=self.request.user.email)
        hackathon_ids = [pr.hackathon.id for pr in participant_registrations]
        return Hackathon.objects.filter(id__in=hackathon_ids)

        

class UserHackathonSubmissionListView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        hackathon_id = self.kwargs['hackathon_id']
        return Submission.objects.filter(user=user, hackathon_id=hackathon_id)

