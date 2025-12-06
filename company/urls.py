from django.urls import path
from company.views import company_register,viewcompany
urlpatterns = [
    path('', company_register),
    path('viewcompany', viewcompany)

]