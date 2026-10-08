from django import forms
from courses.models import Person, Course


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name"]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "description"]