from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Experience, Education, Project, Blog, Comment, Reply
from django.utils.timezone import now

def home(request):
    """Fetch latest 4 blogs and other homepage content."""
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all()
    blogs = Blog.objects.order_by('-date_published')[:4]  # Latest 4 blogs

    return render(request, 'main/home.html', {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'projects': projects,
        'blogs': blogs,
    })

def all_blogs(request):
    """Fetch all blogs ordered by date."""
    blogs = Blog.objects.order_by('-date_published')
    return render(request, 'main/all_blogs.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    """Display blog details along with comments and replies."""
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.all().order_by('-date_posted')  # Use 'date_posted' instead of 'created_at'
    
    return render(request, 'main/blog_detail.html', {
        'blog': blog,
        'comments': comments,
    })


def add_comment(request, blog_id):
    """Add a comment to a blog post."""
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        name = request.POST.get('name')
        content = request.POST.get('content')

        if name and content:
            Comment.objects.create(blog=blog, name=name, content=content)

    return redirect('blog_detail', blog_id=blog.id)

def add_reply(request, comment_id):
    """Add a reply to a comment."""
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        name = request.POST.get('name')
        content = request.POST.get('content')

        if name and content:
            Reply.objects.create(comment=comment, name=name, content=content)

    return redirect('blog_detail', blog_id=comment.blog.id)

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
import os
from .models import Profile

def download_cv(request):
    profile = get_object_or_404(Profile, id=1)  # Assuming you have only one profile
    file_path = profile.cv_file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            # Set Content-Disposition to 'attachment' to force download
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404("CV file not found")