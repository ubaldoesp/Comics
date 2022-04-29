from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)