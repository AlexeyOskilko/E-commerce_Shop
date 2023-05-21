from django.shortcuts import redirect, render


def index(request):
    return render(request, 'website/index-2.html',locals())