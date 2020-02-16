from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolino

def index(request):
	wszystko = Portfolino.objects.all()
	context = {'wszystko': wszystko}
	return render(request, 'index.html', context)