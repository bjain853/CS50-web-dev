from django.shortcuts import render

tasks=["foo","bar","baz"]
# Create your views here.
'''
Return a HttpResponse whose 
content is filled with the result of 
calling django.template.loader.render_to_string() 
with the passed arguments.
'''
def index(request):
    return render(request,"todoApp/index.html",{
        "tasks":tasks
    })

def add(request):
    return render(request,"todoApp/add.html")