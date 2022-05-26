from django.shortcuts import render, HttpResponse, render
from django.http import JsonResponse
import json
from serpapi import GoogleSearch
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate,login as loginuser,logout
from .models import User




@api_view(['GET'])
def home(request):
    json_data = open('api/data.json')   
    data1 = json.load(json_data) # deserialises it
    data2 = json.dumps(data1) # json formatted string
    temp_dict = {}
    for idx in range(0,len(data1)):
        temp_dict[idx]=data1[idx]
    json_data.close()
    print(temp_dict)
    return Response({'data':temp_dict.values()})

#sends the list of images
@api_view(['GET'])
def search(request,item):
    # print(item)
    params = {
    "api_key": "7b7f2472af9f352f6a653ab36725882f92b33bf6382ed9b70ce5f475faaa24f6",
    "engine": "google",
    "ijn": "0",
    "q": item,
    "google_domain": "google.com",
    "num": "100",
    "tbm": "isch"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    temp2_dict = {}
    for idx in range(len(results["images_results"])):
        temp2_dict[idx] = results["images_results"][idx]
    temp3 = temp2_dict.values()
    resp = []
    for item in temp3:
        resp.append(item['original'])
    # return render(request,'images.html',context={'context':temp2_dict.values()})
    
    return Response({'context':resp})

# @api_view(['GET'])
# def send(request):
#     return Response({"running":"running"})
@api_view(['POST'])
def login(request):
    name = request.POST.get('name')
    user = User(name=name)
    results = user.save()
    return Response({'response':'user added succesfully'})

@api_view(['GET'])
def fun(request):
    return render(request,'show_data.html')

@api_view(['GET','POST'])
def save_data(request):
    if request.method == 'POST':
        return Response( {'response':request.data})
    



    