from django.urls import path
from . import views

app_name = "enroll_request"
urlpatterns = [
  path('', views.landing_page, name="landing_page"),
  path('create-course/', views.create_course, name="create_course"),
  path('course-list/', views.course_list, name="course_list"),
  path('course-details/<int:id>/', views.course_details, name="course_details"),
  path('update-course/<int:id>/', views.update_course, name="update_course"),
  path('delete-course/<int:id>/', views.delete_course, name="delete_course"),
  path('enroll-in-course/<int:id>/', views.enroll_in_course, name="enroll_in_course"),
]