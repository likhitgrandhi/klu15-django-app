from django.http import HttpResponse
from rango.models import *
from rango.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/rango/noticeboard/')
    else:
        form = UserCreationForm()
    return render(request, 'rango/signup.html', {'form': form})


@login_required(login_url='/rango/login')
def index(request):
    course_list = Course.objects.filter(department__studentprofile__user=request.user.pk)
    form = CategoryForm()
    context_dict = {'courses': course_list, 'form': form}

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Hello this is rango about page </br> <a href='/rango/'>Rango</a>")


def show_course(request, course_name_slug):
    context_dict = {}

    try:
        student = StudentProfile.objects.filter(department__studentprofile__user=request.user.pk)
        course = Course.objects.get(slug=course_name_slug)
        pages = Page.objects.filter(course=course)
        context_dict['pages'] = pages
        context_dict['course'] = course
        context_dict['students'] = student
    except Course.DoesNotExist:
        context_dict['pages'] = None
        context_dict['course'] = None
        context_dict['students'] = None
    return render(request, 'rango/category.html', context_dict)


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                # probably better to use a redirect here.
            return show_course(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}

    return render(request, 'rango/add_page.html', context_dict)


@login_required(login_url='/rango/login')
def show_notices(request):
    department = Department.objects.filter(studentprofile__user=request.user.pk)
    form = NoticeboardForm()
    course_list = Course.objects.filter(department__studentprofile__user=request.user.pk)
    student = StudentProfile.objects.filter(department__studentprofile__user=request.user.pk)
    notice_list = Noticeboard.objects.all()
    context_dict = { 'department': department, 'notices': notice_list, 'form': form, 'username': request.user.username, 'courses': course_list,
                    'student': student,}

    if request.method == 'POST':
        form = NoticeboardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("/rango/noticeboard/")
        else:
            print(form.errors)

    return render(request, 'rango/noticeboard.html', context_dict)
