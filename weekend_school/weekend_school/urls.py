from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('admin/', admin.site.urls),
  path('', include('enrollment_request.urls', namespace='enroll_request')),
  path('user-account/', include('user_account.urls', namespace='user_account')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)