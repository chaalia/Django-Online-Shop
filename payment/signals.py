from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
from django.core.mail import EmailMessage
import weasyprint
from django.conf import settings
from io import BytesIO
from django.template.loader import render_to_string


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)

        # make the order as paid
        order.paid = True
        order.save()

    # CREATE INVOICE email
    subject = 'My shop - invoice num {}'.format(order.id)
    message = 'you ca find he invoice attached below'
    email = EmailMessage(subject, message, 'rjabchaalia1@gmail.com', [order.mail])

    # generate pdf
    html = render_to_string('orders/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint(settings.STATIC_URLS_DIRS + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach pdf file
    email.attach('order_{}.pdf'.format(order.id),
                 out.getvalue(),
                 'application//pdf')
    # send email
    email.send()


valid_ipn_received.connect(payment_notification)