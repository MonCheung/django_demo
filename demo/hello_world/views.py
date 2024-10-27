from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def hello_world(request):
    return HttpResponse('Hello World')


def test_api(request):
    return JsonResponse({'message': 'Hello World'})


def page_view(request):
    return render(request, 'page.html')
