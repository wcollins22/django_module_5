from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request, response
from app.forms import Stringform, nhform, cd_form, lsform
# Create your views here

def hey_name(request):
    if request.GET:
        name = request.GET["name"]
        return render(request, "base.html", {"name": name})
    else:
        return render(request, "base.html")

def age(request):
    if request.GET:
        year = int(request.GET["year"])
        answer = 2050 - year
        return render(request, "home.html", {"year":year, "answer":answer})
    else:
        
        return render(request, "home.html")

def order(request):
    if request.GET:
        d = int(request.GET["d"])
        b = int(request.GET["b"])
        f = int(request.GET["f"])
        dd = d * 1.0
        bb = b * 4.5
        ff = f * 1.5
        total = float(dd + bb + ff)
        return render(request, "gb.html", {"dd":dd, "bb":bb, "ff":ff, "total":total})
    else:
        return render(request, "gb.html")

def string_splosion(request):
    form = Stringform(request.GET)
    if form.is_valid():
        string = form.cleaned_data["string"]
        result = ""
        for i in range(len(string)):
            result = result + string[:i+1]
        return render(request, "ss.html", {"form": form,"string":string, "result": result})
    else:
        return render(request, "ss.html", {"form": form})

def near_hundred(request):
    form = nhform(request.GET)
    if form.is_valid():
        number = form.cleaned_data["number"]
        return render(request, "nh.html", {"form":form, "number":number})
    else:
        return render(request, "nh.html", {"form": form})

def cat_dog(request):
    form = cd_form(request.GET)
    if form.is_valid():
        string = form.cleaned_data["string"]
        cat = 0
        dog = 0
        cat_dog = False
        for i in range(len(string)):
            if string[i:i+3] == "cat":
                cat += 1
            elif string[i:i+3] == "dog":
                dog += 1
        if cat == dog:
            cat_dog = True
        return render(request, "cd.html", {"form": form, "cat_dog": cat_dog})
    else:
        return render(request, "cd.html", {"form": form})

def ls(request):
    form = lsform(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]
        result = 0
        if a == b == c:
            pass
        elif b == c:
            result = a
        elif a == c:
            result = b
        elif a == b:
            result = c
        else:
            result = (a+b+c)
        return render(request, "ls.html", {"form": form, "result": result})
    else:
        return render(request, "ls.html", {"form": form})
