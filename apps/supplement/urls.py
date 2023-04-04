from django.urls import path
from apps.supplement.views import index,group_index  

urlpatterns = [
    path("", index, name="supplement_create"),
    path("group", group_index, name="group"),
]