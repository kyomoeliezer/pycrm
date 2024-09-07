from django.core.mail import send_mail
from pycrm.settings import EMAIL_HOST
def send_email_common(title,desc,emails):

    data=''
    data=send_mail(
        title,
        desc,
        EMAIL_HOST,
        emails,
        fail_silently=False,
    )
    print(data)
