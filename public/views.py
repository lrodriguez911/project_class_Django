from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def hello_world(request):
    return HttpResponse('Hello world from django')

def index(request):
    if(request.method == 'GET'):
        title = "title if req method is GET"
    else:
        title = "title when access by another method"
        
    list_courses = [1,2,3,4,5]
    return render(request, "public/index.html", {
        "hi": "hello",
        "today": datetime.now,
        "courses": list_courses
    })

def greet(request, name):
    return HttpResponse(request, "public/index.html", {
        "hi": "hello",
        "today": datetime.now
    })

def projects(request, year, month):
    return HttpResponse(f""" 
                        <h1> I am making a project</h1>
                        year:{year} month:{month}""")