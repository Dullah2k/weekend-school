from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import CourseForm
from .models import Course, EnrollmentReques


def landing_page(request):
  return render(request, "enrollment_request/index.html")

def create_course(request):
  if request.method == 'POST':
    course_form = CourseForm(request.POST, request.FILES)
    if course_form.is_valid():
      course_form.save()
      messages.success(request, "Course added successfully")
      return redirect('enroll_request:course_list')
    else:
      messages.error(request, "Something went wrong please try again")
  else:
    course_form = CourseForm()
  return render(request, 'enrollment_request/course/create_course.html', {'course_form' : course_form})

@staff_member_required
def staff_course_list(request):
  courses = Course.objects.all()
  return render(request, "enrollment_request/course/staff_course_list.html", {'courses':courses})

def course_list(request):
  courses = Course.objects.all()
  return render(request, "enrollment_request/course/course_list.html", {'courses':courses})

def course_details(request, id):
  course = get_object_or_404(Course, id=id)
  return render(request, "enrollment_request/course/course_details.html", {'course':course})

@staff_member_required
def update_course(request, id):
  course = get_object_or_404(Course, id=id)
  if request.method == 'POST':
    course_form = CourseForm(request.POST, request.FILES, instance=course)
    if course_form.is_valid:
      course_form.save()
      messages.success(request, f"{course.name} Details Updated successfully")
      return redirect("enroll_request:course_details", id=id)
    else:
      messages.error(request, "Something went wrong")
  else:
    course_form = CourseForm(instance=course)
  return render(request, "enrollment_request/course/update_course.html", {'course_form':course_form})

@staff_member_required
def delete_course(request, id):
  course = get_object_or_404(Course, id=id)
  if request.method == "POST":
    course.delete()
    messages.success(request, f"{course.name} Has been successfully deleted")
    return redirect("enroll_request:course_list")
  return render(request, "enrollment_request/course/course_confirm_delete.html", {'course':course})

def enroll_in_course(request, id):
  course = get_object_or_404(Course, id=id)
  student = request.user.student

  if not course.is_enrollment_open():
    messages.error(request, "Enroll deadline has passed")
    return redirect("enroll_request:course_details", id=course.id)
  
  created = EnrollmentReques.objects.get_or_create(student=student, course=course)
  if created:
    messages.success(request, "Enrollment request submitted")
  else:
    messages.info(request, "You have already requested to enroll in this course")
  return redirect("enroll_request:course_details", id=course.id)

@staff_member_required
def enroll_request_list(request):
  enroll_requests = EnrollmentReques.objects.all()
  return render(request, "enrollment_request/enroll_request/request_list.html", {'enroll_requests':enroll_requests}) 

@staff_member_required
def enroll_request_details(request, id):
  enroll_request = get_object_or_404(EnrollmentReques, id=id)
  return render(request, "enrollment_request/enroll_request/request_details.html", {"enroll_request":enroll_request})