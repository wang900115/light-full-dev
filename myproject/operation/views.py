from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Event , Showinfo
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
## 展示活動
def list_event(request):
    events = Event.objects.all() 
    return render(request, 'operation/list_event.html', {'events': events})

## 展示該活動的場次
def query_event_shows(request, event_uid):
    event = get_object_or_404(Event, uid=event_uid)
    shows = Showinfo.objects.filter(event_uid=event)
    return render(request, 'operation/query_event_shows.html', {'event': event, 'shows': shows})

## 刪除動作(要有登入)
@login_required(login_url='/user/login/')
def delete_event(request, event_uid):
    if request.method == 'POST':
        event = get_object_or_404(Event, uid=event_uid)
        event.delete()
        return redirect('list-event')
    return HttpResponse("Invalid request method", status=400)

## 更新動作(要有登入)
@login_required(login_url='/user/login/')
def update_event(request, event_uid):
    if request.method == 'POST':
        event = get_object_or_404(Event, uid=event_uid)
        event.title = request.POST.get('title', event.title) or event.title
        event.startdate = request.POST.get('startdate', event.startdate) or event.startdate
        event.enddate = request.POST.get('enddate', event.enddate) or event.enddate
        event.save()
        return redirect('list-event')
    return HttpResponse("Invalid request method", status=400)
    
## 登出
@login_required(login_url='/user/login/')
def logout_view(request):
    logout(request)
    return redirect('list-event')