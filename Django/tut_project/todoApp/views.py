from django.shortcuts import render

tasks=["foo","bar","baz"]
# Create your views here.
def index(request):
    return render(request,"todoApp/index.html",{
        "tasks":tasks
    })

def add(request):
    return render(request,"todoApp/add.html")