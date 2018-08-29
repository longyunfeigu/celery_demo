from django.shortcuts import render
from django.http import HttpResponse
from app01.tasks import add
# Create your views here.
def asynch(request, *args, **kwargs):
    # build.delay()
    add.delay(1,2)
    return HttpResponse('hello')