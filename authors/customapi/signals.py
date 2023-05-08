from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.conf import settings

from oscarapi.signals import oscarapi_post_checkout


@receiver(oscarapi_post_checkout)
def send_email_on_checkout(sender, order, **kwargs):
    subject = render_to_string('oscar/communication/emails/commtype_order_placed_subject.txt', {'order': order})
    html_message = render_to_string('oscar/communication/emails/commtype_order_placed_body.html', {'order': order})
    message = render_to_string('oscar/communication/emails/commtype_order_placed_body.txt', {'order': order})
    from_email = settings.OSCAR_FROM_EMAIL
    recipient_list =  [order.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True, html_message=html_message)
