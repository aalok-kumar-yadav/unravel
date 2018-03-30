from django.shortcuts import render


def sin_up(request):
    return render(request, 'sinup.html', None)


def log_in(request):
    return render(request, 'login.html', None)


