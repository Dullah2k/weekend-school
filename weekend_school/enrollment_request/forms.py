from django import forms
from . models import Course, Student, EnrollmentReques

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ["name", "description", "deadline", "image"]
    widgets = {
      "deadline" : forms.DateTimeInput(
        attrs={
        'type' : 'datetime-local',
      }),
    }

class EnrollmentRequestForm(forms.ModelForm):
  class Meta:
    model = EnrollmentReques
    fields = []
