from django.shortcuts import render

# Create your views here.

def archives(request):
    return render(request, 'main/archives.html')


def blog(request):
    return render(request, 'main/blog.html')


def demo(request):
    return render(request, 'main/demo.html')


def index(request):
    return render(request, 'main/index.html')


def page(request):
    return render(request, 'main/page.html')


def single(request):
    return render(request, 'main/single.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')