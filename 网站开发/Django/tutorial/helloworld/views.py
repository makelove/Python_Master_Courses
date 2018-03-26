from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the helloworld index.")
    return render(request,template_name='helloworld/index.html')