from django.urls import path

from .views import (
    ConferredDegreeAutocomplete,
    DiplomaCreateView,
    DiplomaDetailView,
    DiplomaListView,
    DiplomaUpdateView,
    SpecialtyAutocomplete,
)

urlpatterns = [
    path("", DiplomaListView.as_view(), name="diploma_list"),
    path("create/", DiplomaCreateView.as_view(), name="diploma_create"),
    path("update/<int:pk>/", DiplomaUpdateView.as_view(), name="diploma_update"),
    path("detail/<int:pk>/", DiplomaDetailView.as_view(), name="diploma_detail"),
    path(
        "specialty-autocomplete/",
        SpecialtyAutocomplete.as_view(),
        name="specialty_autocomplete",
    ),
    path(
        "conferred-degree-autocomplete/",
        ConferredDegreeAutocomplete.as_view(),
        name="conferred_degree_autocomplete",
    ),
]
