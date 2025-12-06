from django.urls import path
from job.views import job,demo
urlpatterns = [
    path('',job),
    path('my',demo)
]