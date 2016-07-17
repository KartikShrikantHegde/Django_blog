from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# This is a function based view, so it takes in request and returns a response

def post_create(request):
    return HttpResponse("<h1>Create<h1>")

# Retrieve operation

def post_detail(request):
    return HttpResponse("<h1>Detail<h1>")

def post_list(request):
    #return HttpResponse("<h1>List<h1>")
    return render(request,"index.html",{})

def post_update(request):
    return HttpResponse("<h1>Update<h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete<h1>")