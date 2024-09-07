from django.db import models
from core.models import BaseDB

class Contact(BaseDB):
    name=models.CharField(max_length=400, verbose_name='Full Name')
    mobile=models.CharField(max_length=300,verbose_name='Main Mobile')
    mobile2 = models.CharField(max_length=300, verbose_name='Mobile 2',blank=True,null=True)
    mobile3 = models.CharField(max_length=300, verbose_name='Mobile 3',blank=True,null=True)
    institution = models.CharField(max_length=300, verbose_name='Institution', blank=True, null=True)
    location=models.ForeignKey('core.Location',on_delete=models.DO_NOTHING,related_name='locationdata',blank=True)

    def __str__(self):
        return self.name

class CustomerQuery(BaseDB):
    ticketNo = models.CharField(max_length=300, verbose_name='TicketNo',unique=True)
    orderno = models.IntegerField( verbose_name='OrderNo', unique=True)
    category=models.ForeignKey('core.Category',on_delete=models.DO_NOTHING,related_name='catgory')
    subcategory = models.ForeignKey('core.Category', on_delete=models.DO_NOTHING, related_name='userauth', blank=True,null=True)
    desc = models.TextField( verbose_name='Description', blank=True, null=True)
    agent=models.ForeignKey('auths.User',on_delete=models.DO_NOTHING,related_name='useragentservice')
    escalatedto = models.ForeignKey('auths.User', on_delete=models.DO_NOTHING, related_name='escalationuser')
    status = models.CharField(max_length=300, verbose_name='TicketStatus',choices=(('Open','Open'),('Attended','Attended'),('Escalated','Escalated'),('Closed','Closed')))

    def __str__(self):
        return self.name


class StatusTracker(BaseDB):
    agent=models.ForeignKey('auths.User',on_delete=models.DO_NOTHING,related_name='usertracker')
    customerquery=models.ForeignKey('servicedesk.CustomerQuery',on_delete=models.DO_NOTHING,related_name='query')
    desc = models.TextField( verbose_name='Description', blank=True, null=True)
    status = models.CharField(max_length=300, verbose_name='TicketStatus', choices=(
    ('Open', 'Open'), ('Attended', 'Attended'), ('Escalated', 'Escalated'), ('Closed', 'Closed')))
    def __str__(self):
        return self.customerquery

