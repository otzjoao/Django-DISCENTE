from django.urls import path
from courses.views import PersonListView

app_name = "courses"

urlpatterns = [
    path("pessoas/", PersonListView.as_view(), name="person_list"),
]