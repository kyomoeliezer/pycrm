from django.urls import path, re_path

from auths.models import Staff
from .views import *


urlpatterns = [

    path("", CategoryLists.as_view(), name="category_lists"),
    path("add-category", CategoryCreate.as_view(), name="add_category"),
    re_path(r"^(?P<pk>[\w-]+)/editcategory$",CategoryUpdate.as_view(),name="update_category"),
    re_path(r"^(?P<pk>[\w-]+)/del-category$",CategoryDelete.as_view(),name="delete_category"),

    path("subcategory", SubCategoryLists.as_view(), name="sub_category_lists"),
    path("add-subcategory", SubcategoryCreate.as_view(), name="add_sub_category"),
    re_path(r"^(?P<pk>[\w-]+)/editsubcategory$",SubCategoryUpdate.as_view(),name="update_sub_category"),
    re_path(r"^(?P<pk>[\w-]+)/del-subcategory$",SubCategoryDelete.as_view(),name="delete_sub_category"),

    path("locations", LocationsLists.as_view(), name="locations"),
    path("add-locations", LocationCreate.as_view(), name="add_location"),
    re_path(r"^(?P<pk>[\w-]+)/editlocations$",LocationUpdate.as_view(),name="update_location"),
    re_path(r"^(?P<pk>[\w-]+)/del-locations$",LocationsDelete.as_view(),name="delete_location"),

]
