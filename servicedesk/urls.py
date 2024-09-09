from django.urls import path, re_path

from auths.models import Staff
from .views import *


urlpatterns = [
    path("popup", PopupView.as_view(), name="popup"),
    path("popup-newx", PopupNewView.as_view(), name="new_popup"),
    path("popdx", PopUpIntroView.as_view(), name="popup_distribute"),

    path("contacts", ContactLists.as_view(), name="contacts"),
    path("QueryLists",QueryLists.as_view(),name='queries'),
    re_path(r"^(?P<pk>[\w-]+)/updatequery",UpdateQuery.as_view(),name='update_query'),
    re_path(r"^(?P<pk>[\w-]+)/attend",AttendQuery.as_view(),name='attend_query')


    ]
