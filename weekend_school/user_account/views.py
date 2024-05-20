from django.shortcuts import render
from .forms import UserRegistrationForm
from enrollment_request.models import Student

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

