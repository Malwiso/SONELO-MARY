from django.shortcuts import render,redirect
from .models import ContactSubmission
from django.contrib import messages  
from .forms import ContactForm

#for index.html
def index(request):
    return render(request, 'MaryPortfolio/index.html')  # Link to the existing template

#for home.html
def home(request):
    return render(request, 'MaryPortfolio/home.html')  # Link to the existing template

#for about.html

def about(request):
    return render(request, 'MaryPortfolio/about.html')  # Link to the existing template


#for project.html

def project(request):
    return render(request, 'MaryPortfolio/project.html')  # Link to the existing template


#for contact.html
def contact(request):
    return render(request, 'MaryPortfolio/contact.html')  # Link to the existing template


#for form submittion and save to the database



def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactSubmission.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")  # Redirect to clear the form
        else:
            messages.error(request, "All fields are required!")

    return render(request, "contact.html")



def view_submissions(request):
    submissions = ContactSubmission.objects.all()  # Querying the model
    return render(request, 'submissions.html', {'submissions': submissions})
