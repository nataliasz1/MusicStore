from django.http import HttpResponse

def index(request):
    return HttpResponse("homepage")

def login(request):
    return HttpResponse("login page")

def profile(request):
    return HttpResponse('profile page')

def catalog(request):
    return HttpResponse('catalog page')