from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from polls.models import *

def index(request):
    items = Building.objects.values_list('name')
    names = []
    for item in items:
        names.append(item[0])
    return render(request, 'index.html', {'buildingitems': names})


def getLatLong(request):
    mybuilding = request.GET['building']
    if mybuilding:
        mylat = Building.objects.filter(name=mybuilding).values_list('latitude')
        mylong = Building.objects.filter(name=mybuilding).values_list('longitude')
        data = {
            'latitude': mylat[0][0],
            'longitude': mylong[0][0]
        }
        return JsonResponse(data)
    return HttpResponse("Permission Denied")


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
                      {'floorval': myfloor, 'roomval': myroom, 'floorimage': myimagefile, 'xpos': mycoordx,
                       'ypos': mycoordy})
    return HttpResponse("Permission Denied")


# used to add room coordinate values to csv
def editor(request):
    items = Building.objects.values_list('name')
    names = []
    for item in items:
        names.append(item[0])
    return render(request, 'editor.html', {'buildingitems': names})


# display editor room image
def editorimage(request):
    myfloor = request.GET['floorvalue']

    if myfloor:
        filename = Floor.objects.filter(name=myfloor).values_list('floorimg')
        myimagefile = str(filename[0][0])
        data = {
            'value': myimagefile
        }
        return JsonResponse(data)
    return HttpResponse("Permission Denied")


# add value to text file from editor
def addToFile(request):
    print('Adding value to file')
    mystring = request.GET['datastring']
    if mystring:
        stringElem = mystring.split(',')
        query = Room.objects.filter(roomNumber=int(stringElem[1])).values_list('id')
        if(len(query)>0):  # value already exists
            data = {
                'result': "That room number is already in our database for this floor!"
            }
        else:
            # add to text file
            myid = Floor.objects.filter(name=stringElem[0]).values_list('id')
            newstring = str(myid[0][0]) + "," + stringElem[1] + "," + stringElem[2] + "," + stringElem[3]
            get_current_site(request)
            with open('static/roomCoordinates.csv', 'a') as f:
                f.write('\n')
                f.write(newstring)
                f.close()
            # insert into database
            allIDs = Room.objects.values_list('id')
            f = Floor.objects.get(id=myid[0][0])
            _, insert = Room.objects.get_or_create(
                id=len(allIDs) + 1,
                floor=f,
                roomNumber=stringElem[1],
                XOffset=stringElem[2],
                YOffset=stringElem[3]
            )
            data = {
                'result': 'Added value "' + newstring + '" to file'
            }
        return JsonResponse(data)
    return HttpResponse("Permission Denied")
