from django.urls import path
# decorator for backwards compatibility
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    # path("register/", views.RegisterView.as_view(), name='register'),
    path("register/", views.register, name='register'),
    path("logout/", views.logout, name='logout'),
    path('valiadte_username/',csrf_exempt(views.UsernameValidationView.as_view()), name='valiad_username'),
    path('valiadte_email/',csrf_exempt(views.EmailValidationView.as_view()), name='valiad_email')
]
