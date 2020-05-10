# Импортируем библиотеку requests
import requests
import json


def new_requests():
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
    dataid = data1.get('id')
    name = data1.get('name')  # Название Bitcoin
    last_updated = data1.get('last_updated')  # Дата обновления
    price_all = data1.get('quote')  # Прайс
    usd = price_all.get('USD')  # Раздел валюты
    price = usd.get('price')  # Цена
    price2 = name , price
    name = post.objects.create(name="name")
    price = Author.objects.create(price="price")
    return name , price

print (new_requests())


