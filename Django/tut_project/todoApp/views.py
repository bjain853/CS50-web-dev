from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# tasks = ["foo","bar","baz"]
class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority",max_value=5,min_value=0)

'''
Return a HttpResponse whose 
content is filled with the result of 
calling django.template.loader.render_to_string() 
with the passed arguments.
'''
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request,"todoApp/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method=="POST" and "tasks" in request.session:
        form=NewTaskForm(request.POST)  #form variable contains data posted by user
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            print(request.session["tasks"])
            return HttpResponseRedirect("/tasks")
    return render(request,"todoApp/add.html",{
        "form":NewTaskForm()
    })