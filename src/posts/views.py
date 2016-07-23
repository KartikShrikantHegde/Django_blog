from urllib import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

# This is a function based view, so it takes in request and returns a response
# render takes in a request

def post_create(request):
    # Not to allow other than staff and admin to create posts.

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    # This is the best method as it directly references the form model and the required fields as well.

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()

        #messege success
        messages.success(request, "Congratulations")
        messages.success(request, "Successfully Created")

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

def post_detail(request, slug=None):

    # get call, but this should not be used.
    #instance = Post.objects.get(id=1)
    #instane = get_object_or_404(Post,title = "Manager")

    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)

    context = {
        "title": instance.title,
        "instance":instance,
        "share_string":share_string,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()

    paginator = Paginator(queryset, 5)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)



    context = {
            "object_list": queryset,
            "title": "List",
        "page_request_var":page_request_var
        }
    return render(request, "post_list.html", context)

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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance = instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        # message success
        messages.success(request, "Congratulations")
        messages.success(request, "<a href='#'>Item</a> Successfully Saved", extra_tags='html_safe')

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance":instance,
        "form":form,
    }

    return render(request, "post_form.html", context)

def post_delete(request, id =None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")