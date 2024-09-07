from django.urls import path, re_path

from auths.models import Staff
from .views import *


urlpatterns = [
    path("popup", PopupView.as_view(), name="popup"),

    ]
