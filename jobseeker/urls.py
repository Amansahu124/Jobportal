from django.urls import path
from jobseeker.views import jobseekerProfile,viewprofile


urlpatterns = [
    path('profile',jobseekerProfile),
    path('viewprofile/<str:name>',viewprofile),
    

]