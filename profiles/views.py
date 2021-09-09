from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm

from .models import Profile

# Create your views here.

def get_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated!')
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)
