from django.shortcuts import render


def map(request):
    return render(request, 'place/map.html', {
        'page_title': 'user map'
    })
