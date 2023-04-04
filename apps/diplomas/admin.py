from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import (
    ConferredDegree,
    Degree,
    Diploma,
    DiplomaTemplate,
    Specialty,
    StudyForm,
)

admin.site.register(StudyForm)
admin.site.register(Specialty)
admin.site.register(Degree)
admin.site.register(ConferredDegree)
admin.site.register(Diploma, SimpleHistoryAdmin)
admin.site.register(DiplomaTemplate)
