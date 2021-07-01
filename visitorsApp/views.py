from django.contrib.sites import requests
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request, 'visitorsApp/home.html')


def visitors(request):
    if request.method == 'POST':
        daytime = request.POST.get('daytime')
        vname = request.POST.get('vname')
        address = request.POST.get('address')
        mobile1 = request.POST.get('mobile1')
        #mobile2 = request.POST.get('mobile2')
        department = request.POST.get('department')
        whom = request.POST.get('whom')
        purpose = request.POST.get('purpose')

        visitor = VisitInfo.objects.create(vname=vname, daytime=daytime, address=address, mobile1=mobile1,
                                           department=department, whom=whom, purpose=purpose)
        visitor.save()
        print("Visitors data saved Successfully.")
        messages.info(request, "visitors Registered Successfully")
        return render(request, 'visitorsApp/visitors.html')
    else:
        return render(request, 'visitorsApp/visitors.html')

def meeting(request):
    if request.method == 'POST':
        daytime = request.POST.get('daytime')
        depart = request.POST.get('depart')
        organiser = request.POST.get('organiser')
        attendee = request.POST.get('attendee')
        purpose = request.POST.get('purpose')
        summary = request.POST.get('summary')
        feedback = request.POST.get('feedback')

        event = MeetingInfo.objects.create(depart=depart, daytime=daytime, organiser=organiser, attendee=attendee,
                                           summary=summary, feedback=feedback, purpose=purpose)
        event.save()
        print("Event/meeting data saved Successfully.")
        messages.info(request, "Meeting registered Successfully")
        return render(request, 'visitorsApp/meeting.html')
    else:
        return render(request, 'visitorsApp/meeting.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password, sep=" ")
        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            print("LoggedIn successfully")
            return redirect('home')
        else:
            print("Invalid credentials")
            messages.info(request, "Invalid Password/Username")
            return redirect('login')
    else:
        return render(request, 'visitorsApp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def allRecord(request):
    if request.method == 'POST':
        info = VisitInfo.objects.all();
        if info:
            print("Myoutput", info)
            return render(request, 'visitorsApp/record.html', {'info': info})

def allMeeting(request):
    if request.method == 'POST':
        info = MeetingInfo.objects.all();
        if info:
            print("Myoutput", info)
            return render(request, 'visitorsApp/emrecord.html', {'info': info})

def record(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        ninfo = VisitInfo.objects.filter(vname__contains=search)
        tinfo = VisitInfo.objects.filter(daytime__contains=search)
        dinfo = VisitInfo.objects.filter(department__contains=search)
        m1info = VisitInfo.objects.filter(mobile1__contains=search)
       # m2info = VisitInfo.objects.filter(mobile2__contains=search)
        pinfo = VisitInfo.objects.filter(purpose__contains=search)
        ainfo = VisitInfo.objects.filter(address__contains=search)
        winfo = VisitInfo.objects.filter(whom__contains=search)
        if ninfo:
            print("Myoutput", ninfo)
            return render(request, 'visitorsApp/record.html', {'info': ninfo})
        elif tinfo:
            print("Myoutput", tinfo)
            return render(request, 'visitorsApp/record.html', {'info': tinfo})
        elif dinfo:
            print("Myoutput", dinfo)
            return render(request, 'visitorsApp/record.html', {'info': dinfo})
        elif ainfo:
            print("Myoutput", ainfo)
            return render(request, 'visitorsApp/record.html', {'info': ainfo})
        elif m1info:
            print("Myoutput", m1info)
            return render(request, 'visitorsApp/record.html', {'info': m1info})
        elif pinfo:
            print("Myoutput", pinfo)
            return render(request, 'visitorsApp/record.html', {'info': pinfo})
        elif winfo:
            print("Myoutput", winfo)
            return render(request, 'visitorsApp/record.html', {'info': winfo})


def emrecord(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        oinfo = MeetingInfo.objects.filter(organiser__contains=search)
        tinfo = MeetingInfo.objects.filter(daytime__contains=search)
        dinfo = MeetingInfo.objects.filter(depart__contains=search)
        pinfo = MeetingInfo.objects.filter(purpose__contains=search)
        if oinfo:
            print("Myoutput", oinfo)
            return render(request, 'visitorsApp/emrecord.html', {'info': oinfo})
        elif tinfo:
            print("Myoutput", tinfo)
            return render(request, 'visitorsApp/emrecord.html', {'info': tinfo})
        elif dinfo:
            print("Myoutput", dinfo)
            return render(request, 'visitorsApp/emrecord.html', {'info': dinfo})
        elif pinfo:
            print("Myoutput", pinfo)
            return render(request, 'visitorsApp/emrecord.html', {'info': pinfo})
