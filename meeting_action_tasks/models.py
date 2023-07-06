from django.db import models
from user_authentication.models import User, Session
from recording_transcription.models import Meeting, Transcript

# Create your models here.
class ActionItem(models.Model):
    action_item_id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=255)
    reporter = models.CharField(max_length=255)
    priority = models.IntegerField()
    due_on = models.DateField()
    status = models.CharField(max_length=255)
    actions = models.TextField()
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)