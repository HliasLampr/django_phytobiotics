from django.shortcuts import render
from .es_call import esearch


def search_index(request):
    results = []
    city_term = ""
    state_term = ""
    if request.GET.get('city') and request.GET.get('state'):
        city_term = request.GET['city']
        state_term = request.GET['state']
    elif request.GET.get('city'):
        city_term = request.GET['city']
    elif request.GET.get('state'):
        state_term = request.GET['state']
    search_term = city_term or state_term
    results = esearch(city=city_term, state=state_term)
    print(results)
    context = {'results': results, 'count': len(results), 'search_term':  search_term}
    return render(request,  'esearch/search.html',  context)
