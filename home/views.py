from django.shortcuts import render


def home(request):
    """ To render the home page """

    return render(request, 'home/index.html')


def policy(request):
    """To render the policy page"""
    return render(request, 'home/policy.html')
