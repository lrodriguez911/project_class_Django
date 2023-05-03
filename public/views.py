from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from public.forms import ContactForm
# Create your views here.
def hello_world(request):
    return HttpResponse('Hello world from django')


def index(request):
    message = None
    if(request.method == 'POST'):
        contact_form = ContactForm(request.POST)
        message = 'I have received your message'
    else:
        contact_form = ContactForm()
    courses = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación',
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🖌🎨',
            'categoria':'Diseño',
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
        {
            'nombre':'Big Data Avanzado',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
    ]
    context = {                
                'courses':courses,
                'mensaje':message,
                'contact_form':contact_form
            }
    return render(request,'public/index.html', context)
    
    
def get_courses(request):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación',
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🖌🎨',
            'categoria':'Diseño',
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
        {
            'nombre':'Big Data Avanzado',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
    ]
    context = {                
        'cursos':listado_cursos
        }
    return render(request,'publica/courses.html',context)

def us(request):
    template = loader.get_template('publica/quienes_somos.html')
    context = {'titulo':'Codo A Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))

def greet(request, name):
    return HttpResponse(request, "public/index.html", {
        "hi": "hello",
        "today": datetime.now
    })

def projects(request, year, month):
    return HttpResponse(f""" 
                        <h1> I am making a project</h1>
                        year:{year} month:{month}""")