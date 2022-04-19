from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from polls.models import *


def index(request):
    items = Building.objects.values_list('name')
    names = []
    for item in items:
        names.append(item[0])
    return render(request, 'index.html', {'buildingitems': names})


def floor(request):
    mybuilding = request.GET['buildingvalue']

    if mybuilding:
        b = Building.objects.get(name=mybuilding)
        items = Floor.objects.filter(building=b.id).values_list('name')
        names = []
        for item in items:
            names.append(item[0])
        data = {
            'values': names
        }
        return JsonResponse(data)
    return HttpResponse("Permission Denied")


def room(request):
    myfloor = request.GET['floorvalue']

    if myfloor:
        f = Floor.objects.get(name=myfloor)
        items = Room.objects.filter(floor=f.id).values_list('roomNumber')
        items.order_by('roomNumber')
        print(str(items))
        names = []
        for item in items:
            names.append(item[0])
        request.session['floorname'] = myfloor
        data = {
            'values': names
        }
        return JsonResponse(data)
    return HttpResponse("Permission Denied")


def image(request):
    myfloor = request.GET['floorvalue']
    myroom = request.GET['roomvalue']

    if myfloor and myroom:
        filename = Floor.objects.filter(name=myfloor).values_list('floorimg')
        myimagefile = str(filename[0][0])
        mycoordx = Room.objects.filter(roomNumber=myroom).values_list('XOffset')
        mycoordx = str(mycoordx[0][0])
        mycoordy = Room.objects.filter(roomNumber=myroom).values_list('YOffset')
        mycoordy = str(mycoordy[0][0])
        return render(request, 'image.html',
                      {'floorval': myfloor, 'roomval': myroom, 'floorimage': myimagefile, 'xpos': mycoordx, 'ypos': mycoordy})
    return HttpResponse("Permission Denied")
