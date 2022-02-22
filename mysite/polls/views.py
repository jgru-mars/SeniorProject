from django.shortcuts import render
from django.http import HttpResponse
import mysite.SQLaccess as sqla

conn = sqla.connectToDB()


def index(request):
    return render(request, 'index.html')


def login(request):
    option = request.POST['options']

    if option:
        filename = sqla.getFloorImg(conn, option)
        myimagefile = open('carrollFloorPlans/' + filename, 'rb')
        response = HttpResponse(content=myimagefile)
        response['Content-Type'] = 'image/jpeg'
        return response
    return HttpResponse("Permission Denied")
