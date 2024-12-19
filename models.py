from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.CharField(max_length=50) # e.g. 'Primary', 'Secondary', 'JC'
    def __str__(self):
        return f"{self.name} ({self.level})"

class Match(models.Model):
    tutor = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tutor_matches')
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='student_matches')
    subjects = models.ManyToManyField(Subject)
    distance_score = models.FloatField(default=0.0)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    matched_on = models.DateTimeField(auto_now_add=True)
