from django.shortcuts import render

def meet_the_team(request):
    return render(request, 'about/meet_the_team.html')

def how_we_work(request):
    return render(request, 'about/how_we_work.html')