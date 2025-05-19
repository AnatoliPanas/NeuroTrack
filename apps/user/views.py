from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

def get_users_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse("List of all users")

