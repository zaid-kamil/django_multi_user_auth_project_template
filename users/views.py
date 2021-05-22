from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import ClientSignUpForm,LawyerSignUpForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
        return render(request, 'registration/register.html')

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

class LawyerSignUpView(CreateView):
    model = User
    form_class = LawyerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'lawyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')