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



def create_ticket(no):
    strdata=''
    if no < 9:
        strdata='000'+str(no)
    elif no < 99:
        strdata='00'+str(no)
    elif no < 999:
        strdata='0'+str(no)
    return 'EC'+strdata