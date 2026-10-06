from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Person

class PersonListView(ListView):
    model = Person
    template_name = "courses/person_list.html"
    context_object_name = "people"
    paginate_by = 10 # Number of people to display per page

class CoursesListView(ListView):
    model = Person
    template_name = "courses/course_list.html"
    context_object_name = "courses"
    paginate_by = 10 # Number of courses to display per page