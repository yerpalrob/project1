from django.shortcuts import render
from django import forms

from . import util

class NewPageForm(forms.Form):
    page = forms.CharField(label="New Page")
    
    content = forms.CharField(label="About")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def add(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
    return render(request, "encyclopedia/add.html", {
        "form": NewPageForm(request.POST)
    })
    
def random(request):
    return render(request, "encyclopedia/random.html")
    
def search(request, search):
    return render(request, "encyclopedia/search.html", {
        "search": search.capitalize()
    })
