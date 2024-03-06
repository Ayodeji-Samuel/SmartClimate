from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.htm')


def about(request):
    return render(request, 'home/about.html')