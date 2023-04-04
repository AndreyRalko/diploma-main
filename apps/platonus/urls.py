from django.urls import path

from .views import StudentAutocomplete

urlpatterns = [
    path("students/", StudentAutocomplete.as_view(), name="student_autocomplete")
]
