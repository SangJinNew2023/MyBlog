from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import logging

logger = logging.getLogger('mysitev1')

from ..models import Question, Answer, Category

def index(request, category_name=None):
    logger.info("Show with the INFO level")
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    category = Category.objects.order_by('id')
    if category_name is None:
        question_list = Question.objects.order_by('-create_date')
    else:
        category_id = Category.objects.get(name=category_name)
        question_list = Question.objects.filter(category_id=category_id)

    #Search
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #Title search
            Q(content__icontains=kw) | #Content search
            Q(answer__content__icontains=kw) | #Answer content search
            Q(author__username__icontains=kw) | #Question author search
            Q(answer__author__username__icontains=kw) #Answer author search
        ).distinct()

    #Patination
    paginator = Paginator(question_list, 10) # 페이지당 10개
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj, 'page':page, 'kw': kw, 'category': category}
    return render(request, 'myboard/question_list.html', context)

def detail(request, question_id):
    category = Category.objects.order_by('id')
    question = get_object_or_404(Question, pk=question_id)
    page=request.GET.get('page', '1')
    answer_list=Answer.objects.filter(question=question).order_by('-voter')
    paginator = Paginator(answer_list, 5)
    page_obj = paginator.get_page(page)
    context = {'answer_list': page_obj, 'question': question,  'category': category}
    return render(request, 'myboard/question_detail.html', context)

