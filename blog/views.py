from django.shortcuts import render, redirect

from .forms import PostCreateForm
from .models import Post
from django.contrib import messages


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def create_post(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Post created successfully!'
            )
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)