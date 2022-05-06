import os

from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from .models import  Item
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def index(request):
    # slider_list = CmsSlider.objects.all()
    return render(request, 'main/index.html')
# , {'slider_list': slider_list}


def about(request):
    return render(request, 'main/about.html')


def accommodation(request):
    return render(request, 'main/accommodation.html')


def gallery(request):
    files = Item.objects.all()
    context = {'files': files}
    return render(request, 'main/gallery.html', context)


def maingallery(request):
    files = Item.objects.all()
    context = {'files': files}
    return render(request, 'main/maingallery.html', context)


def send_gmail(request):
    if request.method == "POST":
        message_name = request.POST.get('name')
        message_email = request.POST.get('email')
        message = request.POST.get('message')

        print(message_name, message_email, message)

        send_mail(
            message_email,
            message,
            '200103114@stu.sdu.edu.kz',
            ['bekzada.abay.2002@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'main/about.html')
    else:
        return render(request, 'main/about.html')






def addFile(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
        prod.save()
        return redirect('/')
    return render(request, 'main/add.html')


def editFile(request, pk):
    prod = Item.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.save()
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'main/edit.html', context)


def deleteFile(request, pk):
    prod = Item.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    return redirect('/')




