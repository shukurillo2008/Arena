from django.shortcuts import render
from . import models
from random import Random
from django.db.models import Q


def index(request):
    arena = models.Arena.objects.all()
    trener =models.Trener.objects.all()
    sport = models.Category.objects.all()
    city = models.City.objects.all()
    region = models.Region.objects.all()

    context = {
        'arena':arena,
        'trener':trener,
        'sport':sport,
        'city':city,
        'region':region
    }
    return render(request, 'index-dark.html', context)


def region_detail(request, id):
    arena = models.Arena.objects.filter(location__region__id = id)
    region = models.Region.objects.all()
    sport = models.Category.objects.all()

    context = {
        "arena":arena,
        'region':region,
        'sport':sport
    }

    return render(request, 'detail.html', context)

def region(request):
    return


def arena(request):
    q = request.GET.get('q')
    if q is not None:
        arena = models.Arena.objects.filter( Q(name__icontains = q) | Q(location__name__icontains = q) | Q(location__region__name__icontains = q))
        region = models.Region.objects.all()
        sport = models.Category.objects.all()
        
    else:
        arena = models.Arena.objects.all()
        region = models.Region.objects.all()
        sport = models.Category.objects.all()


    context = {
        "arena":arena,
        "region":region,
        "sport":sport
    }

    return render(request, 'detail.html', context)



def arena_detail(request, id):
    arena = models.Arena.objects.get(id = id)
    img = models.ImageArena.objects.filter(arena = arena)
    treners = models.Trener.objects.filter(arena = arena)
    region = models.Region.objects.all()
    sport = models.Category.objects.all()

    context = {
       "arena" : arena,
       "img" : img,
       'treners' : treners,
       'region':region,
       'sport':sport
    }

    return render(request, "arena_detail.html", context)


def trener(request):

    q = request.GET.get('q')

    if q is not None:
        trener = models.Trener.objects.filter( Q(name__icontains=q) | Q(l_name__icontains = q) | Q(sport__name__icontains = q))
        region = models.Region.objects.all()
        sport = models.Category.objects.all()
    else:
        trener = models.Trener.objects.all()
        region = models.Region.objects.all()
        sport = models.Category.objects.all()

    context = {
        "treners":trener,
        'region':region,
        'sport':sport
    }

    return render(request, 'trener.html', context)


def trener_detail(request, id):
    trener = models.Trener.objects.get(id = id)
    region = models.Region.objects.all()
    sport = models.Category.objects.all()

    context = {
        "trener":trener,
        'region':region,
        'sport':sport
    }

    return render(request, "trener_detail.html", context)


def sport_trener(request, id):
    trener = models.Trener.objects.filter(sport__id = id)
    region = models.Region.objects.all()
    sport = models.Category.objects.all()

    context = {
        "treners":trener,
        'region':region,
        'sport':sport
    }

    return render(request, 'trener.html', context)







