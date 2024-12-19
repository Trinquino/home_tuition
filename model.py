from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extend the default Django user with roles and other details
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    subjects_offered = models.ManyToManyField('core.Subject', blank=True)
    # Additional fields like age range, etc. can be added for tutors
    # For students, store the required subjects and headcount
    student_headcount = models.IntegerField(default=1, blank=True, null=True)
    educational_level = models.CharField(max_length=50, blank=True, null=True)  # e.g. 'Primary', 'Secondary'

