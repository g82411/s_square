from django.shortcuts import render
#excape XSS String
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from api.models import *
STATUSCODE = {
    "ADDUSERSUCCESS":"201",
    "VOTESUCCESS":"202",
    "ADDGROUPSUCCESS":"203",
    "JOINSUCCESS":"204",
    "SEARCHSUCCESS":"206",
    "UPDATEUSERNAMESUCCESS":"205",
    "PARAMETERMISS":"301",
    "TOOLONGPARAMETER":"302",
    "SQLERROR":"303",
    "NOGROUPNAME":"304",
    "UNDEFINEUSERID":"305",
    "UNDEFINECHOOSE":"306",
    "FACKUERROR":"307",
    "UNDEFINEGROUPID":"308",
    "USERNOTINGROUP":"309",
}
# Create your views here.
@csrf_exempt
def useradd(request):
    def getRandomString(length):
        result = ''
        POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        for i in range(length):
            result += random.choice(POOL)
        return result
    callback = "userdata"
    response = {}
    if not "username" in request.POST:
        response["status"] = STATUSCODE["PARAMETERMISS"]
    else:
        username = escape(request.POST["username"])
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
        
        