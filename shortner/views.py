import json
from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def create(request):
    if request.body:
        link = json.loads(request.body.decode("utf-8"))
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        print(uid)
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect("https://" + url_details.link)
