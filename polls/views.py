# -*-coding:utf-8 -*-
import sys
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# 以下为防止中文字符乱码
# ----------------------------------------------
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# ----------------------------------------------
# 2016年12月14日14:52:38


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("问题编号 %s." % question_id)

def results(request, question_id):
    response = "结果编号 %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("处理编号 %s." % question_id)
