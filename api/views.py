import random
import sys
import traceback
import json
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
#excape XSS String
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from api.models import *
STATUSCODE = {
    "ADDUSERSUCCESS":"201",
    "VOTESUCCESS":"202",
    "ADDGROUPSUCCESS":"203",
    "LOGINSUCCESS":"204",
    "SEARCHSUCCESS":"206",
    "GETMONSTERPOSITION":"205",
    "PARAMETERMISS":"301",
    "TOOLONGPARAMETER":"302",
    "USERNOTEXISTS":"310",
    "SQLERROR":"303",
    "NOGROUPNAME":"304",
    "UNDEFINEUSERID":"305",
    "UNDEFINECHOOSE":"306",
    "FACKUERROR":"307",
    "UNDEFINEGROUPID":"308",
    "USERNOTINGROUP":"309",
    "NOMONSTER":"404"
}
# Create your views here.
def useradd(request):
    def getRandomString(length):
        result = ''
        POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        for i in range(length):
            result += random.choice(POOL)
        return result
    callback = "userdata"
    response = {}
    if not "username" in request.GET:
        response["status"] = STATUSCODE["PARAMETERMISS"]
    else:
        username = escape(request.GET["username"])
        session = getRandomString(32)
        while User.objects.filter(session=session).count() > 0:
            session = getRandomString(32)
        try:
            newUser = User(session=session,uname=username)
            newUser.save()
            response["session"] = session
            response["userName"] = username
            response["status"] = STATUSCODE["ADDUSERSUCCESS"]
        except Exception as e:
            response["status"] = STATUSCODE["SQLERROR"]
            print e
    data = '%s(%s);' % (callback,json.dumps(response))
    return HttpResponse(data,content_type="application/javascript")
        
def userlogin(request):
    callback = "loginstat"
    response = {}
    if not "session" in request.GET:
        response["status"] = STATUSCODE["PARAMETERMISS"]
    else:
        session = escape(request.GET["session"])
        print session
        try:
            if User.objects.filter(session=session).count() > 0:
                userData = User.objects.get(session=session).uid
                response["uid"] = userData
                response["status"] = STATUSCODE["LOGINSUCCESS"]
                response["msg"] = "LOGINSUCCESS"
            else:
                response["status"] = STATUSCODE["USERNOTEXISTS"]
                response["msg"] = "USERNOTEXISTS"
        except Exception as e:
            response["status"] = STATUSCODE["SQLERROR"]
            traceback.print_exc(file=sys.stdout)
            response["msg"] = "SQLERROR"
    data = '%s(%s);' % (callback,json.dumps(response))
    return HttpResponse(data,content_type="application/javascript")
def getMonster(request):
    callback = "mPosition"
    response = {}
    if not ("user" in request.GET and "lat" in request.GET and "lon" in request.GET):
        response["status"] = STATUSCODE["PARAMETERMISS"]
    else:
        lat = float(request.GET["lat"])
        lon = float(request.GET["lon"])
        userID = request.GET["user"]
        try:
            QueryData = MonsterPosition.objects.filter(latitude__range=(lat-0.01,lat+0.01)
                ,longitude__range=(lon-0.01,lon+0.01))
            if QueryData.count() > 0:
                response["data"] = []
                for monster in QueryData:
                    response["data"].append(
                    	{"name":monster.mid.mname,
                    "lat":monster.latitude,
                    "lon":monster.longitude,
                    "mid":monster.mid_id}
                    )
                    
                response["status"] = STATUSCODE["GETMONSTERPOSITION"]
                response["msg"] = "GETMONSTERPOSITION"
            else:
                response["status"] = STATUSCODE["NOMONSTER"]
                response["msg"] = "NOMONSTER"
        except Exception as e:
            response["status"] = STATUSCODE["SQLERROR"]
            traceback.print_exc(file=sys.stdout)
            response["msg"] = "SQLERROR"
    data = '%s(%s);' % (callback,json.dumps(response))
    return HttpResponse(data,content_type="application/javascript")
