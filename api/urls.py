"""Comics_Marvel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from comics.views import ComicsView, get_object, get_param
from rest_framework.routers import DefaultRouter

from users import views as user_views

router=DefaultRouter()
router.register(r'users',user_views.UsersViewSet, basename='users')

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('searchComics/',ComicsView.as_view()),
    path('searchComics/<str:search>', get_object),
    path('searchComics/detail/<int:id>',get_param),
    path('', include(router.urls))
]
