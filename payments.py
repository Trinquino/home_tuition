
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from decimal import Decimal

def generate_paynow_qr(payment_details):
    """
    Generates a PayNow QR Code.

    Args:
        payment_details (dict): Contains 'UEN', 'amount', 'reference' keys.
    Returns:
        BytesIO: QR code image bytes for rendering or saving.
    """
    uen = payment_details.get('UEN', '')
    amount = Decimal(payment_details.get('amount', 0))
    reference = payment_details.get('reference', '')

    # Build the PayNow QR Code payload
    payload = f"""
        000201
        010212
        26
        0013SG.PAYNOW
        02{len(uen):02}{uen}
        5303704
        54{len(f"{amount:.2f}"):02}{amount:.2f}
        5802SG
        59{len(reference):02}{reference}
        6304
    """.replace("\n", "").strip()

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(payload)
    qr.make(fit=True)
    
    # Create QR Code image
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return buffer
