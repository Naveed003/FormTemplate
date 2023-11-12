import sqlite3

from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from main.models import admin
import hashlib
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
from main.GoogleForm import form
from docx import Document
from django.core.files import uploadedfile
from django.shortcuts import redirect
def home(request):
    return render(request, 'home.html')

    # return render(request, 'uploadtemplate.html')


def mainButtonHandling(request):
    if request.POST['action'] == "upload":
        return render(request, 'form.html')
    else:
        db=contracts.objects.all()
        var=[]
        temp=[]
        for i in db:
            temp.append(i.name)
            temp.append(i.url)

            var.append(temp)
            temp=[]
        return render(request, 'fill.html',{'lists':var})


def Login(request):
    emplid = request.POST['emplid']
    pwd = request.POST['pwd']


    try:
        dbhash = admin.objects.get(emplid=str(emplid))
        print(dbhash)

    except Exception:
        return render(request, 'home.html')

    pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    pwd=str(dbhash)
    print(type(pwd), type(dbhash))
    if (pwd == str(dbhash)):
        print("sffssg")
        return render(request, 'uploadtemplate.html')

    return render(request, 'form.html')


def filesave(request):
    file = request.FILES['docfile']
    name = file.name
    try:

        db=contracts.objects.get(name=name)
        if str(db.name)==str(name):
            return render(request,'home.html')
    except Exception:
        pass

    doc = Document(file)
    table = doc.tables[0]
    rows = table.rows
    variables = []
    for i in rows:
        for j in i.cells:
            if len(j.text) > 1 and j.text[0] == '(' and j.text[-1] == ')' and j.text[
                                                                              1:len(j.text) - 1] not in variables:
                variables.append(j.text[1:len(j.text) - 1])

    response = form(variables, name)
    obj = contracts(name=name, file=file, url=response[1], formid=response[0])
    obj.save(())
    return render(request, 'home.html')
    # name=new.upload


def fill(request):

    name=str(request.POST['action'])

    return  render(request,'base.html')