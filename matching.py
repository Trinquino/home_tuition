from decimal import Decimal
from django.conf import settings
from .models import Match

def calculate_commission(subject_count, student_count, base_rate=Decimal(settings.COMMISSION_RATE)):
    # Assume base_rate is 0.5 for 50%
    # Commission = (Number of subjects * Number of students) * (Base Rate * Subject Fee)
    # Subject fee can be standardized or fetched from tutor’s rate. For simplicity, assume a flat subject fee of $100.
    subject_fee = Decimal(100)
    commission = subject_count * student_count * subject_fee * base_rate
    return commission

def find_matches(tutor, student):
    # Implement a matching logic based on location, subjects, etc.
    # For demonstration:
    shared_subjects = tutor.subjects_offered.filter(level=student.educational_level)
    if shared_subjects.exists():
        distance_score = 10.0  # Dummy proximity score calculation
        commission = calculate_commission(
            subject_count=shared_subjects.count(),
            student_count=student.student_headcount
        )
        match = Match.objects.create(
            tutor=tutor,
            student=student,
            distance_score=distance_score,
        )
        match.subjects.set(shared_subjects)
        match.commission_amount = commission
        match.save()
        return match
    return None

