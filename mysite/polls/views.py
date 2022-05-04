import os

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
        myfloorob = Floor.objects.get(name=myfloor)  # get actual floor object
        mycoordx = Room.objects.filter(floor=myfloorob, roomNumber=myroom).values_list('XOffset')
        mycoordx = str(mycoordx[0][0])
        mycoordy = Room.objects.filter(floor=myfloorob, roomNumber=myroom).values_list('YOffset')
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


# add value to text file from editor. Splits code into each file, building, floor, and room
def addToFile(request):
    print('Adding value to file')
    mystring = request.GET['datastring']
    myfile = request.GET['file']
    if mystring and myfile:
        if myfile == 'buildingNames.csv':
            with open('static/' + myfile, 'a') as f:
                f.write('\n')
                f.write(mystring)
                f.close()
            # insert into database
            stringElem = mystring.split(',')
            allIDs = Building.objects.values_list('id')
            _, insert = Building.objects.get_or_create(
                id=len(allIDs) + 1,
                name=stringElem[0],
                longitude=stringElem[2],
                latitude=stringElem[1]
            )
            data = {
                'result': 'Added value "' + mystring + '" to file ' + myfile
            }
            return JsonResponse(data)
        elif myfile == 'floorTable.csv':
            stringElem = mystring.split(',')
            # add to text file
            myid = Building.objects.filter(name=stringElem[2]).values_list('id')
            newstring = stringElem[0] + "," + stringElem[1] + "," + str(myid[0][0])
            with open('static/' + myfile, 'a') as f:
                f.write('\n')
                f.write(newstring)
                f.close()
            # insert into database
            allIDs = Floor.objects.values_list('id')
            b = Building.objects.get(id=myid[0][0])
            _, insert = Floor.objects.get_or_create(
                id=len(allIDs) + 1,
                name=stringElem[0],
                floorimg=stringElem[1],
                building=b
            )
            data = {
                'result': 'Added value "' + newstring + '" to file ' + myfile
            }
            return JsonResponse(data)
        elif myfile == 'roomCoordinates.csv':
            stringElem = mystring.split(',')
            myid = Floor.objects.filter(name=stringElem[0]).values_list('id') # get id of floor
            myfloor = Floor.objects.get(id=myid[0][0]) # get actual floor object
            query = Room.objects.filter(floor=myfloor, roomNumber=int(stringElem[1])).values_list('id')
            if (len(query) > 0):  # value already exists
                data = {
                    'result': "That room number is already in our database for this floor!"
                }
            else:
                # add to text file
                newstring = str(myid[0][0]) + "," + stringElem[1] + "," + stringElem[2] + "," + stringElem[3]
                with open('static/' + myfile, 'a') as f:
                    f.write('\n')
                    f.write(newstring)
                    f.close()
                # insert into database
                allIDs = Room.objects.values_list('id')
                _, insert = Room.objects.get_or_create(
                    id=len(allIDs) + 1,
                    floor=myfloor,
                    roomNumber=stringElem[1],
                    XOffset=stringElem[2],
                    YOffset=stringElem[3]
                )
                data = {
                    'result': 'Added value "' + newstring + '" to file ' + myfile
                }
            return JsonResponse(data)
    return HttpResponse("Permission Denied")


# get list of image files from static directory
def getFiles(request):
    myfiles = []
    for root, dirs, files in os.walk("static/"):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg'): # only want image files
                myfiles.append(file)
    data = {
        'filename': myfiles
    }
    return JsonResponse(data)

