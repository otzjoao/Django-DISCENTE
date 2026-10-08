from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from courses.forms import PersonForm, CourseForm
from courses.models import Person, Course

class PersonListView(ListView):
    model = Person
    template_name = "courses/person_list.html"
    context_object_name = "people"
    paginate_by = 10 # Number of people to display per page

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    paginate_by = 10 # Number of courses to display per page

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "courses/person_form.html"
    context_object_name = "person"
    # fields = ["first_name", "last_name"]
    success_url = reverse_lazy("courses:person_list")
    login_url = reverse_lazy("admin:login")

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    context_object_name = "course"
    success_url = reverse_lazy("courses:course_list")
    login_url = reverse_lazy("admin:login")
