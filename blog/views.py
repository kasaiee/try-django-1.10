from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import (
    Paginator, 
    EmptyPage, 
    PageNotAnInteger
    )
from forms import BlogForm
from models import Blog


def list(request):

    posts = Blog.objects.all().order_by('-updateDateTime')

    query = request.GET.get('q')
    if query:
        posts = posts.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                )


    paginator = Paginator(posts, 5) # Show 5 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, 'list.html', context)


def detail(request, id):
    post = get_object_or_404(Blog, id=id)

    context = {
        'post': post
    }
    return render(request, 'detail.html', context)


def create(request):
    form = BlogForm(request.POST or None, request.FILES,)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        messages.success(request, _('created successfully! <a href="/">See the item</a>'), extra_tags='alert alert-success safe')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit(request, id=None):
    instance = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, _('updated successfully!!'), extra_tags='alert alert-success')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)


def delete(request, id):
    post = get_object_or_404(Blog, id=id)
    if post.delete():
        messages.success(request, _('item deleted successfully!'), extra_tags='alert alert-success')
    return render(request, 'detail.html', {'post': post})

