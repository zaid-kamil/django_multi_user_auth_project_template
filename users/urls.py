from django.conf.urls import include
from django.urls import path

from .views import dashboard, register,ClientSignUpView,LawyerSignUpView

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup', register, name='register'),
    path('accounts/signup/client', ClientSignUpView.as_view(), name='client_register'),
    path('accounts/signup/lawyer', LawyerSignUpView.as_view(), name='lawyer_register'),
    path('oauth/', include('social_django.urls')),
]