from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

#Returns the homepage by request.
def home_view(request):
    return render(request, 'home.html')

#Returns the about page by request.
def about_view(request):
    return render(request, 'about.html')

#Returns the contact page by request.
def contact_view(request):
    return render(request, 'contact.html')

#Verifies the username and password fields for logging into the private application's dashboard page.
#Incorrect post will return empty username and password fields for new input and post verification.
#User account must have been created by the django superuser/admin beforehand.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('private:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form })
