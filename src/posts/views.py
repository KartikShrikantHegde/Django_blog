from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.

# This is a function based view, so it takes in request and returns a response
# render takes in a request

def post_create(request):
    # This is the best method as it directly references the form model and the required fields as well.

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    # This is not a recommended method
    # if request.method == "POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
    #     Post.objects.create(title = title)

    context = {
         "form": form,
     }

    return render(request, "post_form.html", context)

# Retrieve operation

def post_detail(request, id=None):
    # get call, but this should not be used.
    #instance = Post.objects.get(id=1)
    #instane = get_object_or_404(Post,title = "Manager")

    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "instance":instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()

    context = {
            "object_list": queryset,
            "title": "List"
        }
    return render(request, "index.html", context)

    # This case works for me as i am still logged into admin page

    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User list"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }



def post_update(request, id = None):

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # messege success
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance":instance,
        "form":form,
    }

    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete<h1>")