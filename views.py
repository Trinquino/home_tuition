
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Match
from .payments import generate_paynow_qr

@login_required
def paynow_qr_view(request):
    user = request.user
    match_id = request.session.get('match_id')
    if not match_id:
        messages.error(request, "No match found for payment.")
        return redirect('dashboard')

    # Fetch the match and calculate the payment amount
    match = Match.objects.get(id=match_id)
    amount = match.commission_amount

    # Define payment details
    payment_details = {
        'UEN': 'S12345678X',  # Replace with your PayNow UEN
        'amount': amount,
        'reference': f"{user.id}-{match_id}",
    }

    # Generate QR code
    qr_image = generate_paynow_qr(payment_details)

    # Serve the QR code as an image
    return HttpResponse(qr_image, content_type="image/png")
