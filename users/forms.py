from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.forms.widgets import RadioSelect

from .models import Client, User,Lawyer

class ClientSignUpForm(UserCreationForm):

    gender = forms.ChoiceField(choices=Client.GENDER_CHOICE, widget=forms.RadioSelect)
    class Meta(UserCreationForm.Meta):
        model= User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.gender = self.cleaned_data.get('gender')
        client.save()

class LawyerSignUpForm(UserCreationForm):

    designation = forms.CharField(widget=forms.TextInput)
    gender = forms.ChoiceField(choices=Lawyer.GENDER_CHOICE, widget=forms.RadioSelect)
    lawyertype = forms.CharField(widget=forms.TextInput)
    experience = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)
    class Meta(UserCreationForm.Meta):
        model= User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lawyer = True
        user.save()
        laywer = Lawyer.objects.create(user=user)
        laywer.gender = self.cleaned_data.get('gender')
        laywer.designation = self.cleaned_data.get('designation')
        laywer.lawyertype = self.cleaned_data.get('lawyertype')
        laywer.experience = self.cleaned_data.get('experience')
        laywer.city = self.cleaned_data.get('city')
        laywer.save()