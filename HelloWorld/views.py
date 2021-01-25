from django.shortcuts import render
from django.http import HttpResponse
from HelloWorld.models import *
# Create your views here.

def index(request):
    # return HttpResponse('老铁，没毛病')
    res_html = render(request,'HelloWorld/index.html',{})
    return HttpResponse(res_html)

def index2(request):
    return HttpResponse('hello index2')


def show_books(request):
    book = BookInfo.objects.all()
    return render(request,'HelloWorld/show_book.html',{
        'books' : book
    })

def detail(request, bid):
    book_info = BookInfo.objects.get(id=bid)
    hero = book_info.heroinfo_set.all()
    return render(request,'HelloWorld/detail.html', {
        'heros' : hero,
        'book': book_info
    })

