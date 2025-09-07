from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def index(request):
    app_name = request.resolver_match.app_name
    return HttpResponse(f'hello {app_name}'.encode('utf-8'))