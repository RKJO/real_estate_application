from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    ctx = {
        'listings' : listings
    }
    
    return render(request, 'pages/index.html', ctx)


def about(request):
    return render(request, 'pages/about.html')
