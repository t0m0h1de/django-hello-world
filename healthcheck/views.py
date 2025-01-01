from django.http import HttpResponse

def readiness(request):
    return HttpResponse("I'm ready.")

def liveness(request):
    return HttpResponse("I'm alive.")