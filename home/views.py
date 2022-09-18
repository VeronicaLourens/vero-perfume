from django.shortcuts import render


def home(request):
    """ To render the home page """

    return render(request, 'home/index.html')
