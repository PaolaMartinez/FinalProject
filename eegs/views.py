from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def index(request):
   return redirect('patient')
# Create your views here.

def patient(request):
    p = models.Patient.objects.all()
    lst = []
    for i in p:
        lst.append((i.id, i.state))
    context = {
        "patient": lst
    }
    # print(lst)
    return render(request, "patients.html", context)

def trial(request):
    if request.method == "POST":
        pat = request.POST.get('patient')
        tmp = pat.split('-')
        string = str(tmp[0])+" - "+str(tmp[1])
        p = models.Patient(int(string[0]), string[1])
        t = models.Trial.objects.filter(patient=p)
        lst = []
        for i in t:
            lst.append(i.id)
        lst2 = []
        for i in range(len(t)):
            lst2.append(i)
        context = {
            "trial": zip(lst, lst2), 
            "channel": ['C3','C4','F3','F4','F7','F8','Fp1','Fp2','O1','O2','P3','P4','T3','T4','T5','T6']
        }
        for i,j in zip(lst, lst2):
            print(i,j)
        return render(request, "trial.html", context)

def channel(request):
    if request.method == "POST":
        tr = request.POST.get('trial')  
        channel = request.POST.getlist('channel')
        trial = request.POST.get('trial')
        lst = []
        for i in channel: 
            c = models.Channel.objects.filter(label=i, trial=trial)
            lst.append(list(map(float,c[0].values.split(','))))

        points = []
        points_def = []
        for i in lst:
            for j in i:
                points.append({'y' : j})
            points_def.append(points)
            points = []
        
        context = {
            "points": points_def,
            "channel": channel
        }
       
    return render(request, "image.html", context)  

            



    