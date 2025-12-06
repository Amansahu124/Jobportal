from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from django.urls import reverse
from django.utils import timezone
from company.models import Company



def job(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    company=Company.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        description = request.POST.get('description')
        job_type = request.POST.get('job_type')

        required_skills = request.POST.get('required_skills', "")
        salary_min = request.POST.get('salary_min')
        salary_max = request.POST.get('salary_max')
        deadline = request.POST.get('deadline')
        print(title, company_name, location, description, job_type, required_skills, salary_min, salary_max, deadline)
        job = Job(
            title=title,
            company_name=company_name,
            location=location,
            description=description,
            job_type=job_type,
            required_skills=required_skills,
            salary_min=salary_min if salary_min else None,
            salary_max=salary_max if salary_max else None,
            deadline=deadline if deadline else None,
        )
        job.save()

        messages.success(request, "Job created successfully!")
        return redirect("/job/")
    return render(request, "job.html", {"jobs": jobs,"company":company})


def demo(request):
    jobs=Job.objects.all()
    return render(request,"viewjob.html",context={"jobs":jobs})