from django.shortcuts import render
from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import json
# Create your views here.
# @api_view(["GET"])
def baseurl(request):
    # return JsonResponse("API Running Successfully",safe=False)
    # return HtmlR('index.html')
    return render_to_response('userinfo/index.html')


def formValidation(request):
    var1 = request.GET['number']
    var2 = request.GET['message']

    # if(int(var1)>10):
    #     res = 'Yes'
    # else:
    #     res = 'No'
    # res = var1>10 ? 'yes':'no'
    # var2 = request.GET['message']
    # return JsonResponse("API Running Successfully",safe=False)
    # return HtmlR('index.html')
    # return HttpResponse("<h1>Number"+var1+"</h1>"+"<h2>Message"+var2+"</h2>")
    return render(request,'userinfo/index.html',{'num':var1,'phn':var2})
    # return render(request,'userinfo/index.html',{'result':res})





# def profile(request):
#     # return JsonResponse("API Running Successfully",safe=False)
#     # return HtmlR('index.html')
#     return HttpResponse('<h1>Rohit</h1><h2>Rohit</h2>')