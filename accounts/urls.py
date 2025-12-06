from django.urls import path
from accounts.views import home,loginView,register,logoutView,view_notifications,search

urlpatterns = [
    path('', home),
    path('login',loginView),
    path('register',register),
    path('logout',logoutView),
    path("notification",view_notifications),
    path("job/viewjob",search)
]