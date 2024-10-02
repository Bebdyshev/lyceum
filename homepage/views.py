from django.shortcuts import render
from django.http import HttpResponse

def say_hello(Request):
    return HttpResponse('hello world~~')