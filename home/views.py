from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponseNotFound
# Create your views here.

API_KEY = 'beabc98af03d476e95f3cc61ca6fef4b'


def base(request):
    #https://newsapi.org/docs/endpoints/sources
    #url = f'https://newsapi.org/v2/top-headlines/sources?apiKey={ API_KEY }'
    # https://newsapi.org/v2/everything?q=space&apiKey=beabc98af03d476e95f3cc61ca6fef4b
    
    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        url = f'https://newsapi.org/v2/everything?q={search}&apiKey=beabc98af03d476e95f3cc61ca6fef4b'
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={ API_KEY }'
    else:
        url = f'https://newsapi.org/v2/top-headlines?category=general&apiKey={ API_KEY }'
    
    response = requests.get(url)
    api_data = response.json()
    
    try:
        article_list = api_data['articles']
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    #print(api_data)
        
    context = { 'articles': article_list, 'active' : category, 'search': search }
    #context['data'] = api_data
    
    return render(request, 'home.html', context=context )
    

#main()