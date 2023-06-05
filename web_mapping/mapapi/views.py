from mapapi.models import Farmer
from django.shortcuts import render

def index(request):
    farmer_locations = Farmer.objects.values()
    context = {'data': list(farmer_locations)}
    return render(request, 'index.html', context)