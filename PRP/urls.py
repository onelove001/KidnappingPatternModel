
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("home", home, name="home"),
    path("data_page", data_page, name="data"),
    path("view_page", view_page, name="view"),
    path("pattern_page", pattern_page, name="pattern"),
    path("female_page", female_page, name="female_page"),
    path("male_page", male_page, name="male_page"),
    path("male_female_page", male_female_page, name="male_female_page"),
    path("zone_page", zone_page, name="zone_page"),
    path("view_2014_2016", view_2014_2016, name="view_2014_2016"),
    path("view_2016_2019", view_2016_2019, name="view_2016_2019"),
    path("view_2019_2021", view_2019_2021, name="view_2019_2021"),
    path("all_year", all_year, name="all_year"),
    path("accuracy", accuracy, name="accuracy"),

]
