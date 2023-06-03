from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User, Group

from topicyeucau.models import Topic, MyTopic
from django.db.models import Count, Q

import datetime

# Create your views here.
def index(request):
    
    year = request.GET.get('year') or datetime.datetime.now().year
    topic_total = [0] * 12
    topic_done = [0] * 12
    
    query = Topic.objects.filter(start_time__year=year).values('start_time__month').annotate(total=Count('id'))
    for report in query:
        month = report.get('start_time__month')
        count = report.get('total')
        topic_total[month] = count
    
    query = MyTopic.objects.filter(start_time__year=year).values('start_time__month').annotate(total=Count('id', filter=Q(status="Hoàn thành")))
    for report in query:
        month = report.get('start_time__month')
        count = report.get('total')
        topic_done[month] = count
    
    
    
    return JsonResponse(data={
        'topic_total_set': topic_total, 
        'topic_done_set': topic_done,
    })
    
def employee_ranking(request):
    
    year = request.GET.get('year') or datetime.datetime.now().year
    query = MyTopic.objects.filter(start_time__year=year).values('employee').annotate(count=Count('id', filter=Q(status="Hoàn thành")))
    ranking = []
    for report in query:
        employee_id = report.get('employee')
        if employee_id is None: continue
        employee_name = User.objects.get(pk=employee_id).userprofile.name
        employee_avatar = User.objects.get(pk=employee_id).userprofile.avatar.url
        count = report.get('count')
        record = dict(
            id=employee_id,
            name=employee_name,
            avatar=employee_avatar,
            count=count,
            rank=0,
        )
        ranking.append(record)
    
    ranking.sort(key=lambda record: record.get('count'), reverse=True)
    rank = 0
    last_count = None
    for r in ranking:
        if last_count is None or r.get('count') < last_count:
            rank +=1
            last_count = r.get('count')
        
        r['rank'] = rank
        
    
    return JsonResponse(ranking, safe=False)

def get_employee_report(request):
    
    year = request.GET.get('year') or datetime.datetime.now().year
    emp_id = request.GET.get('emp_id')
    
    if emp_id is None: return HttpResponseNotFound()
    employee = User.objects.get(pk=emp_id)
    if employee is None or not employee.groups.filter(pk=3).first(): return HttpResponseNotFound()
    
    query = MyTopic.objects.filter(start_time__year=year, status="Hoàn thành", employee=emp_id).values('start_time__month').annotate(count=Count('id'))
    dataset = [0] * 12
    
    for report in query:
        month = report.get('start_time__month')
        dataset[month] = report.get('count')
    
    return JsonResponse(data=dict(
        employee=dict(name=employee.userprofile.name),
        dataset=dataset,
    ))

def get_member_ranking(request):
    
    year = request.GET.get('year') or datetime.datetime.now().year
    month = request.GET.get('month') or datetime.datetime.now().month
    
    query = Topic.objects.filter(start_time__year=year, start_time__month=month).values('author').annotate(count=Count('id'))
    ranking = []
    for report in query:
        author_id = report.get('author')
        if author_id is None: continue
        _name = User.objects.get(pk=author_id).userprofile.name
        _avatar = User.objects.get(pk=author_id).userprofile.avatar.url
        count = report.get('count')
        record = dict(
            id=author_id,
            name=_name,
            avatar=_avatar,
            count=count,
            rank=0,
        )
        ranking.append(record)
    
    ranking.sort(key=lambda record: record.get('count'), reverse=True)
    rank = 0
    last_count = None
    for r in ranking:
        if last_count is None or r.get('count') < last_count:
            rank +=1
            last_count = r.get('count')
        
        r['rank'] = rank
        
    
    return JsonResponse(ranking, safe=False)