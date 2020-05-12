import json
import requests
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .tasks import get_money
from django.http import HttpResponseRedirect, HttpResponse


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

def get_price(request):
    url_param = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        "X-CMC_PRO_API_KEY": "d61bca4c-e9d3-40b9-8d82-abf9b057ffbd",
        "Accept": "application/json"
    }
    params = {"id": 1}
    response = requests.get(
        url_param,
        params=params,
        headers=headers,
    )
    result = json.loads(response.text)
    data = result.get('data')
    data1 = data.get('1')  # Номер ID
    #dataid = data1.get('id')
    name = data1.get('name')  # Название Bitcoin
    #last_updated = data1.get('last_updated')  # Дата обновления
    price_all = data1.get('quote')  # Прайс
    usd = price_all.get('USD')  # Раздел валюты
    price = usd.get('price')  # Цена
    price = float('{:.2f}'.format(price))
    Post.objects.create(name=name, price=price)
    return HttpResponseRedirect("/")