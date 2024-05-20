from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = "user_account"
urlpatterns = [
  path('create-account/', views.register_user, name="register_user"),
  path('login/', views.CustomLoginView.as_view(), name="login"),
  path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]