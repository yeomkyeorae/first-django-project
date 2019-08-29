from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request, 'services/index.html')


def artii(request):
    return render(request, 'services/artii.html')


def artii_result(request):
    query = request.GET
    string = query.get('string')
    font = query.get('font')
    response = requests.get('http://artii.herokuapp.com/make?text={}&font={}'.format(string, font))
    context = {
        'result': response.text,
    }
    return render(request, 'services/artii_result.html', context)