from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.core.files.storage import FileSystemStorage
from .models import Image
from .forms import ImageForm
import datetime


def index(request):
    images = Image.objects.all()
    return render(request, "index.html", {"images": images})


def upload(request):
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = form.save()
        form.date = datetime.datetime.now()
        form.save()
        return HttpResponsePermanentRedirect("/", {"images": form})
    else:
        form = Image()
        return render(request, "upload.html")


def delete(request, id):
    try:
        image = Image.objects.get(id=id)
        image.delete()
        return HttpResponseRedirect("/")
    except Image.DosNotExist:
        return HttpResponseNotFound("<h2>Картинка не найдена</h2>")