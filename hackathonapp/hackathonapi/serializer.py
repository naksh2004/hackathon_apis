from rest_framework import serializers
from .models import Hackathon,ParticipantRegistration,Submission

class HackathonSerializer(serializers.ModelSerializer):
    #participants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Hackathon
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class ParticipantRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantRegistration
        fields = '__all__'



