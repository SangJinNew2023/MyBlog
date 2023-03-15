from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    # page = request.GET.get('page', '1')
    posts = PostModel.objects.all()
    # paginator = Paginator(posts, 6)
    # page_obj = paginator.get_page(page)
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user #add author
            instance.save()
            return redirect('myblog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
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