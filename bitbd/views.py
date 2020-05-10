from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .tasks import get_money
from django.http import HttpResponseRedirect


# получение данных из бд
def index(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        posts = posts,

    return render(request, 'blog/index.html', {'posts': posts})


def new_requests(request):
    get_money.delay()
    return HttpResponseRedirect("/")


