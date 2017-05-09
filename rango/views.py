from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict) 
def about(request):
	return HttpResponse("Hello this is rango about page </br> <a href='/rango/'>Rango</a>")

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)