from django.db import models
from django.conf import settings
from django.utils import timezone

class Course(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  deadline = models.DateTimeField()
  image = models.ImageField(upload_to='course_images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
  def is_enrollment_open(self):
    return timezone.now() < self.deadline
  
class Student(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  profile_image = models.ImageField(upload_to='user_images/', blank=True, null=True)
  created_at =  models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name}"
  
class EnrollmentReques(models.Model):
  STATUS_CHOICES = [
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
  ]
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
  requested_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.student} - {self.course} ({self.status})"
  




