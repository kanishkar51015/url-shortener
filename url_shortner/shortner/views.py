from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
import urllib3
from django.views.decorators.csrf import csrf_exempt
from .models import URL
import uuid
import pymongo
from pymongo import MongoClient
import os, json


def index(request):
    request.COOKIES['key'] = str(uuid.uuid1())
    response = render(request,"shortner/index.html")
    response.set_cookie('key', str(uuid.uuid1()))
    return response

def short(request):    
    if request.method == 'POST':
        user = request.COOKIES.get('key')
        url = request.POST['link']
        if url.find('<name of your domain>') != -1:
            return render(request, 'index.html', {'status': 'Funny'})  #dynamic data onto your HTML template
        http = urllib3.PoolManager()
        valid = False
        if url.startswith("http"):            
            url = url    
        else:
            url = "http://"+url
        
        try:
            ret = http.request('GET',url)
            if ret.status == 200:
                valid = True
        except Exception as e:
            valid = False
            
        if valid == True:
            new_url = str(uuid.uuid4())[:5]
            surl = "<name of your domain>"+new_url
            sch = {'uid' : user, 'link' : url, 'new' : surl}
            coll.insert_one(sch)
            return render(request, 'short.html', {'user':user, 'url': url, 'new':surl})           #dynamic data onto your HTML template
        else:
            return render(request, 'index.html', {'status': False})
    return redirect('/')

def mailing(request):
    if request.method == 'POST':        
        mail = request.POST['mail']                  #requesting data entered by user
        user = request.COOKIES.get('key')
        details = coll.find_one({"uid": user})
        details = parse_json(details)
        mssg = f"Hey,\nThanks for using <name of your domain>.\nThe new url for {details['link']} is:\n{details['new']}.\nRegards,\n<your name>\n<your contact details>"
        surl = details['new']
        try:
            send_mail("Shorten URLs", mssg, settings.EMAIL_HOST_USER, [mail])
            return render(request, 'short.html', {'user':user, 'new':surl, 'success': True})        #dynamic data onto your HTML template
        except Exception as e:
            return render(request, 'short.html', {'user':user, 'new':surl, 'success': False})       #dynamic data onto your HTML template
    return redirect('/')

def openurl(request, uid):  
    if uid != "": 
        details = coll.find_one({"new": "<name of your domain>"+uid})
        details = parse_json(details)
        if details:
            full_url = details['link']
            if full_url.startswith("http"): 
                return redirect(full_url)
            else:        
                return redirect("http://"+full_url)
        else:
            return HttpResponse(404)