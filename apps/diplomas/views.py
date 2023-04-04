from dal import autocomplete
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.utils.html import format_html
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.platonus.models import Student

from .filters import DiplomaAdminFilter, DiplomaFilter
from .forms import DiplomaForm, DiplomaStatusForm
from .models import ConferredDegree, Diploma, Specialty


class DiplomaListView(LoginRequiredMixin, ListView):
    model = Diploma
    paginate_by = 10
    template_name = "diplomas/diploma_list.html"

    def get_queryset(self):
        user = self.request.user

        queryset = Diploma.objects.all().select_related(
            "degree", "conferred_degree", "generated_by", "specialty"
        )

        if not user.is_staff and not user.is_superuser:
            queryset = queryset.filter(generated_by=user)

        filterset_class = self.get_filterset_class()

        self.filterset = filterset_class(self.request.GET, queryset=queryset)

        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["filterset"] = self.filterset
        return context

    def get_filterset_class(self):
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            return DiplomaAdminFilter

        return DiplomaFilter


class DiplomaCreateView(LoginRequiredMixin, CreateView):
    form_class = DiplomaForm
    template_name = "diplomas/diploma_create.html"

    def get(self, request, *args, **kwargs):
        student_id = self.request.GET.get("student_id")

        if not student_id:
            messages.error(
                request,
                "Выберите нужного студента в поле ниже и нажмите 'Создать диплом'",
            )
            return redirect("home")

        student = Student.objects.using("platonus").filter(id=student_id).first()

        if not student:
            messages.error(
                request,
                "Выберите нужного студента в поле ниже и нажмите 'Создать диплом'",
            )
            return redirect("home")

        self.student = student

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)

        self.object.generated_by = self.request.user
        self.object.save()

        return response

    def get_initial(self):
        initial = super().get_initial()

        student_id = self.request.GET.get("student_id")

        if student_id and not initial.get("firstname"):
            try:
                student = self.student
            except AttributeError:
                student = (
                    Student.objects.using("platonus").filter(id=student_id).first()
                )

            if student:
                initial["platonus_id"] = int(student_id)
                initial["iin"] = student.iin
                initial["firstname_kk"] = student.firstname
                initial["lastname_kk"] = student.lastname
                initial["patronymic_kk"] = student.patronymic
                initial["firstname_en"] = student.firstname_en
                initial["lastname_en"] = student.lastname_en
                initial["firstname_ru"] = student.firstname
                initial["lastname_ru"] = student.lastname
                initial["patronymic_ru"] = student.patronymic

        return initial


class DiplomaUpdateView(UserPassesTestMixin, UpdateView):
    form_class = DiplomaForm
    queryset = Diploma.objects.all()
    template_name = "diplomas/diploma_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.generated_by == self.request.user or self.request.user.is_staff


class DiplomaDetailView(UserPassesTestMixin, DetailView):
    model = Diploma

    def test_func(self):
        obj = self.get_object()
        return obj.generated_by == self.request.user or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["status_form"] = DiplomaStatusForm(
            initial={"status": self.object.status}
        )

        return context

    def post(self, request, *args, **kwargs):
        form = DiplomaStatusForm(request.POST, request.FILES)

        if form.is_valid():
            self.object = self.get_object()

            self.object.status = form.cleaned_data["status"]
            self.object.save()

            context = self.get_context_data(**kwargs)

            return self.render_to_response(context)


class SpecialtyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Specialty.objects.none()

        qs = Specialty.objects.all()

        if self.q:
            qs = qs.filter(
                Q(name_kk__icontains=self.q)
                | Q(name_en__icontains=self.q)
                | Q(name_ru__icontains=self.q)
                | Q(code__icontains=self.q)
            )

        return qs

    def get_result_label(self, result):
        return format_html(
            "{} {} | {} | {} ({})",
            result.code,
            result.name_kk,
            result.name_en,
            result.name_ru,
            "ОП" if result.is_educational_program else "специальность",
        )


class ConferredDegreeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return ConferredDegree.objects.none()

        qs = ConferredDegree.objects.all()

        if self.q:
            qs = qs.filter(
                Q(name_kk__icontains=self.q)
                | Q(name_en__icontains=self.q)
                | Q(name_ru__icontains=self.q)
            )

        return qs

    def get_result_label(self, result):
        return format_html(
            "{} | {} | {}", result.name_kk, result.name_en, result.name_ru
        )
