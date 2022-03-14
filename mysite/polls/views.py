from django.shortcuts import render
from django.http import HttpResponse
import mysite.SQLaccess as sqla
from polls.models import *


conn = sqla.connectToDB()


def index(request):
    return render(request, 'index.html')


def floor(request):
    mybuilding = request.POST['buildings']

    if mybuilding:
        b = Building.objects.get(name=mybuilding)
        items = Floor.objects.filter(building=b.id).values_list('name')
        names = []
        for item in items:
            names.append(item[0])
        return render(request, 'floor.html', {'flooritems': names})
    return HttpResponse("Permission Denied")


def image(request):
    myfloor = request.POST['floornames']

    if myfloor:
        #filename = sqla.getFloorImg(conn, myfloor)
        f = Floor.objects.get(name=myfloor)
        filename = Floor.objects.filter(name=f.name).values_list('floorimg')
        myimagefile = open('carrollFloorPlans/' + str(filename[0][0]), 'rb')
        response = HttpResponse(content=myimagefile)
        response['Content-Type'] = 'image/jpeg'
        return response
    return HttpResponse("Permission Denied")
