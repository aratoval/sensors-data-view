from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def under_construction(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())
