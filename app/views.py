from django.shortcuts import render,redirect
from .models import Post, Comment

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def comment(request, post_id):
    
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        post1 = Post.objects.get(id=post_id)
        Comment.objects.create(author=author, text=text, post=post1)
        return redirect('comment', post_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'comment.html', {'post_id': post ,'post': post.comments.all()})
