from django.shortcuts import *


def index(request):
    context = {}
    return render(request, "index.html", context)


def home(request):
    context = {}
    return render(request, "home.html", context)


def data_page(request):
    context = {}
    return render(request, "data.html", context)


def view_page(request):
    context = {}
    return render(request, "view.html", context)


def pattern_page(request):
    context = {}
    return render(request, "pattern.html", context)


def female_page(request):
    context = {}
    return render(request, "by_female.html", context)


def male_page(request):
    context = {}
    return render(request, "by_male.html", context)


def male_female_page(request):
    context = {}
    return render(request, "female_male.html", context)


def zone_page(request):
    context = {}
    return render(request, "by_zone.html", context)


def view_2014_2016(request):
    context = {}
    return render(request, "view_2014_2016.html", context)


def view_2016_2019(request):
    context = {}
    return render(request, "view_2016_2019.html", context)


def view_2019_2021(request):
    context = {}
    return render(request, "view_2019_2021.html", context)


def all_year(request):
    context = {}
    return render(request, "all_year.html", context)


def accuracy(request):
    context = {}
    return render(request, "accuracy.html", context)