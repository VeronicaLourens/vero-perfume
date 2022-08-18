from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    To render user profile page with user's personal information.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)


