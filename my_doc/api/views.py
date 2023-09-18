# -*- coding: utf-8 -*-
"""File that handels request and response from webserver."""
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    """Function that returns http respones after request.
    
    :param request:
    :rtype object:
    """
    return HttpResponse("Response")