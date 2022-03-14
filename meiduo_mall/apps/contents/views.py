import imp
from django.shortcuts import render
from django.views import View
from django import http

# Create your views here.
class IndexView(View):

    def get(request):

        return render(request,'index.html')
