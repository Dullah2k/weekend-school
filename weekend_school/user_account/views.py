from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from enrollment_request.models import Student

class CustomLoginView(LoginView):
  def get_success_url(self):
    user = self.request.user
    if user.is_staff:
      return reverse_lazy("enroll_request:staff_course_list")
    else:
      return reverse_lazy("enroll_request:course_list")

def register_user(request):
  if request.method == "POST":
    reg_form = UserRegistrationForm(request.POST)
    if reg_form.is_valid():
      new_user = reg_form.save(commit=False)
      new_user.set_password(reg_form.cleaned_data['password'])
      new_user.save()
      Student.objects.create(user=new_user)
      return render(request, 'user_account/register_done.html', {'new_user':new_user})
  else:
    reg_form = UserRegistrationForm()
  return render(request, "user_account/register.html", {'reg_form':reg_form})

