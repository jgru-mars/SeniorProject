from django.shortcuts import render
from django.http import HttpResponse
import uuid

allowed_users = {"nate", "ted", "upperclass"}
# This stores the list of valid sessions to determine if a valid user is logged in
active_sessions = dict()


def index(request):
    return render(request, 'index.html')


def login(request):
    # Ensure the username was provided, otherwise redirect them back
    option = request.POST['options']
    if not option:
        return render(request, 'index.html')

    # If the user is allowed, set a random session cookie if one doesn't exist
    if option.lower() in allowed_users:
        return HttpResponse("Login Successful")

    return HttpResponse("Permission Denied")


