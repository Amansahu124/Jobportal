from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from job.models import Job
from company.models import Company
def home(request):
    keyword = request.GET.get('keyword')
    location = request.POST.get('location')

    jobs = Job.objects.all()

    # Filter if search values are provided
    if keyword:
        jobs = jobs.filter(title__icontains=keyword)
    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'index.html', {"jobs": jobs})


# Register User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
    

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('/register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('/register')

        # Create new user
        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('/login')

    return render(request, 'register.html')


# Login User
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
       

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login')

    return render(request, 'login.html')


# Logout User
def logoutView(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('/login')

def view_notifications(request):
    notifications = [
        {"message": "Your profile has been viewed.", "time": "2 hours ago"},
        {"message": "New job posted in your field.", "time": "5 hours ago"},
        {"message": "Application status updated.", "time": "1 day ago"},
    ]
    
    return render(request, "notification.html", {"notifications": notifications})


def search(request):
    keyword = request.POST.get("keyword", "").strip()
    search_type = request.POST.get("type", "all")  # 'all', 'jobs', 'companies'

    jobs = []
    companies = []

    if keyword:  # if keyword is not empty
        if search_type == "jobs":
            jobs = Job.objects.filter(title__icontains=keyword)
        elif search_type == "companies":
            companies = Company.objects.filter(company_name__icontains=keyword)
        else:  # all
            jobs = Job.objects.filter(title__icontains=keyword)
            companies = Company.objects.filter(company_name__icontains=keyword)

    context = {
        "jobs": jobs,
        "companies": companies,
        "keyword": keyword,
        "search_type": search_type,
    }

    return render(request, "viewjob.html", context)

