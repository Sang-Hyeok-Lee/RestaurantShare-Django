from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):

    return render(request, 'shareRes/index.html')
    
def restaurantDetail(request,res_id):
    return render(request, 'shareRes/restaurantDetail.html')
    
def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):

    return render(request, 'shareRes/categoryCreate.html')
