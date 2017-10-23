from django.shortcuts import render


def Index(request):
    context = {}
    return render(request, 'volunteerapp/index.html', context)
