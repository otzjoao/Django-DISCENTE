from django.urls import path
from courses.views import PersonListView, PersonUpdateView, CourseListView, CourseUpdateView

app_name = "courses"

urlpatterns = [
    path("pessoas/", PersonListView.as_view(), name="person_list"),
    path("cursos/", CourseListView.as_view(), name="course_list"),
    path("pessoas/<int:pk>/editar/", PersonUpdateView.as_view(), name="person_update"),
    path("cursos/<int:pk>/editar/", CourseUpdateView.as_view(), name="course_update"),
]