from django import template
from django.contrib.auth.models import Group
from auths.models import User
register = template.Library()

@register.simple_tag
def is_manager(request):
     return request.user.groups.filter(name='manager').exists()

@register.simple_tag
def _can_create_processing_shipment(user):
      if  user.perm.filter(name='create_processing_shipment').exists():
           return True
      return False

@register.simple_tag
def _can_view_processing_shipment(user):
      if  user.perm.filter(name='can_view_processing_shipment').exists():
           return True
      return False
@register.simple_tag
def can_delete_request(user):
      if  user.perm.filter(name='can_delete_request').exists():
           return True
      return False

@register.simple_tag
def can_create_request(user):
    print(user)
    if  user.perm.filter(name='can_create_request').exists():

      print(True)
      return True
    print(False)
    return False
