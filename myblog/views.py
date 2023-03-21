from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    posts = PostModel.objects.all()
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user #add author
            instance.save()
            return redirect('myblog-index')
    else:
        form = PostModelForm()
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page)
    context = {
        'posts': page_obj,
        'form': form,
    }
    return render(request, 'myblog/index.html', context)

@login_required(login_url='users-login')
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('myblog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request,'myblog/post_detail.html', context)

@login_required(login_url='users-login')
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('myblog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'myblog/post_edit.html', context)

@login_required(login_url='users-login')
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('myblog-index')
    context = {
        'post': post,
    }
    return render(request, 'myblog/post_delete.html', context)