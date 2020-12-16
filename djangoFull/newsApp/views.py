from django.shortcuts import render, HttpResponse, redirect
from .models import News, RegistrationData, Article
from .forms import RegistrationForm, RegistrationModal
from django.contrib import messages


# Create your views here.

def home(request):
    #------NewsArticleHomePageImportant
    articles = Article.objects.all()


    #------LatestNewsHomePageBeginnerNotImportant
    context = {
        'articles' : articles,
        'name' : 'Musa Sönmez',
        'number' : 2557
    }
    return render(request, 'home.html', context)


def newsP(request):

    obj = News.objects.get(id=1)

    context = {
        'data' : obj,
    }
    return render(request, 'news.html', context)


def newsDate(request, year):
    article_list = News.objects.filter(pub_date__year = year)

    context = {
        'year' : year,
        'article_list' : article_list,
    }

    return render(request, 'newsdate.html', context)


def contact(request):
    return render(request, 'contact.html')


def register(request):
    form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone']
        )

        myregister.save()
        messages.add_message(request, messages.SUCCESS, 'You have signup successfully')
    return redirect('register')


def modelform(request):
    form = RegistrationModal()
    context = {
        'form' : form
    }
    return render(request, 'modelform.html', context)


def addModelForm(request):
    form = RegistrationModal(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'You have signup successfully')
        return redirect('modelform')