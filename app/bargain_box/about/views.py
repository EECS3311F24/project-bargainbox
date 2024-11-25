from django.shortcuts import render

def meet_the_team(request):
    return render(request, 'about/meet_the_team.html')