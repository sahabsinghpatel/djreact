from django.shortcuts import redirect, render
from .models import BlogPost, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    blog_posts=BlogPost.objects.all().order_by('-pub_date', '-pub_time')
    page=request.GET.get('page')
    paginator = Paginator(blog_posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts':posts})

def search(request):
    query=request.GET.get('query')
    if query is not None:
        blog_title=BlogPost.objects.all().filter(title__contains=query).order_by('-pub_date', '-pub_time')
        blog_content=BlogPost.objects.all().filter(content__contains=query).order_by('-pub_date', '-pub_time')
        blog_posts=(blog_title | blog_content).distinct()
        page=request.GET.get('page')
        paginator = Paginator(blog_posts, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'blog/search.html', {'posts':posts, "query":query})
    else:
        return redirect('/blog/')

def blog_post(request, slug):
    post=BlogPost.objects.get(slug=slug)
    comments=Comment.objects.all().filter(post=post).order_by('-post_date', '-post_time')
    return render(request, 'blog/blog_post.html', {'post':post, 'comments':comments})

@login_required(login_url='/profile/login')
def post_comment(request):
    if request.method=="POST":
        username=request.user.username
        user=User.objects.get(username=username)
        post_id=request.POST.get('cpost')
        post=BlogPost.objects.get(sno=post_id)
        comment=request.POST.get('comment')
        user_comment=Comment.objects.create(commenter=user, post=post, comment=comment)
        user_comment.save()
        return redirect(f'/blog/{post.slug}/#comments')
    else:
        return redirect('/blog/')
