from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the helloworld index.")
    context = {'title': '欢迎光临首页', 'name': 'xiaoMing', 'age': 14, 'class': '高一3班', 'scores': [73, 84, 68, 93]}
    return render(request,template_name='helloworld/index.html',context=context)