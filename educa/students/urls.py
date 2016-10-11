from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
]