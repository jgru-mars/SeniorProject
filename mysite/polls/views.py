from django.shortcuts import render
from django.http import HttpResponse
from polls.models import *


def index(request):
    items = Building.objects.values_list('name')
    names = []
    for item in items:
        names.append(item[0])
    return render(request, 'index.html', {'buildingitems': names})


def floor(request):
    mybuilding = request.POST['buildingnames']

    if mybuilding:
        b = Building.objects.get(name=mybuilding)
        items = Floor.objects.filter(building=b.id).values_list('name')
        names = []
        for item in items:
            names.append(item[0])
        return render(request, 'floor.html', {'flooritems': names})
    return HttpResponse("Permission Denied")


def room(request):
    myfloor = request.POST['floornames']

    if myfloor:
        f = Floor.objects.get(name=myfloor)
        items = Rooms.objects.filter(floor=f.id).values_list('roomNumber')
        print(str(items))
        names = []
        for item in items:
            names.append(item[0])
        request.session['floorname'] = myfloor
        return render(request, 'room.html', {'roomitems': names, 'floorname': myfloor})
    return HttpResponse("Permission Denied")


def image(request):
    myfloor = request.session['floorname']
    myroom = request.POST['roomnames']

    if myfloor and myroom:
        filename = Floor.objects.filter(name=myfloor).values_list('floorimg')
        myimagefile = str(filename[0][0])
        mycoordx = Rooms.objects.filter(roomNumber=myroom).values_list('XOffset')
        mycoordx = str(mycoordx[0][0])
        mycoordy = Rooms.objects.filter(roomNumber=myroom).values_list('YOffset')
        mycoordy = str(mycoordy[0][0])
        return render(request, 'image.html', {'floorimage': myimagefile, 'xpos': mycoordx, 'ypos': mycoordy})
    return HttpResponse("Permission Denied")
