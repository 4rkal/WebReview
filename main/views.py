from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Topic, site
from .forms import CreateNewList

# Create your views here.

def index(response,id):
    ls = Topic.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for site in ls.site_set.all():
                if response.POST.get("c" + str(site.id)) == "clicked":
                    site.verified = True
                else:
                    site.verified = False

                site.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.site_set.create(text=txt, verified=False)
            else:
                print("invalid input")

    return render(response, "main/sitelist.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def docs(response):
    return render(response, "main/docs.html", {})

def addsite(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Topic(name=n)
            t.save()
        return HttpResponseRedirect("/%i"%t.id)
    else:
        form = CreateNewList(response)

    form = CreateNewList()
    return render(response, "main/addsite.html", {"form":form})

def viewall(response):
    return render(response, "main/all.html", {})