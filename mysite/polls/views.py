from django.shortcuts import render
from django.http import HttpResponse
import mysite.SQLaccess as sqla

conn = sqla.connectToDB()


def index(request):
    return render(request, 'index.html')


def floor(request):
    building = request.POST['buildings']

    if building:
        items = sqla.getFloors(conn, building)
        return render(request, 'floor.html', {'flooritems': items})
    return HttpResponse("Permission Denied")


def image(request):
    myfloor = request.POST['floornames']

    if myfloor:
        print("THE VALUE OF THE FLOOR IS "+str(myfloor))
        filename = sqla.getFloorImg(conn, myfloor)
        myimagefile = open('carrollFloorPlans/' + filename, 'rb')
        response = HttpResponse(content=myimagefile)
        response['Content-Type'] = 'image/jpeg'
        return response
    return HttpResponse("Permission Denied")
