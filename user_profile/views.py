from django.shortcuts import redirect, render
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def profile_view(request):
    
    current_user = Profile.objects.get(user__id = request.user.id)
    form = ProfileForm(instance=current_user)
    if request.method =="GET":
        context ={'form': form}
        
        return render(request, 'main/profile.html', context)
    
    if request.method == 'POST':
        form = ProfileForm( request.POST,
            request.FILES,
            instance=current_user)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            
            return redirect("dashboard")