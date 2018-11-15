from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from polls.models import Question
from django.urls import reverse
from django.template import loader

# Create your views here.
"""我们不再需要导入 loader 和 HttpResponse 。不过如果你还有其他函数（比如说 detail, results, 和 vote ）需要用到它的话，
就需要保持 HttpResponse 的导入。"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

"""
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))
"""

"""
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")
"""
"""
def detail(request,question_id):
    return HttpResponse("You're looking at queetion %s." %question_id)
"""
"""
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(request,'polls/detail.html',{'question':question})
    
为什么我们使用辅助函数 get_object_or_404() 而不是自己捕获 ObjectDoesNotExist 异常呢？还有，为什么模型 API 不直接抛出 
ObjectDoesNotExist 而是抛出 Http404 呢？
因为这样做会增加模型层和视图层的耦合性。指导 Django 设计的最重要的思想之一就是要保证松散耦合。一些受控的耦合将会被包含在 
django.shortcuts 模块中    
"""
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = "You're looking at the results of queetion %s."
    return HttpResponse(response %question_id)

def vote(requset,question_id):
    return HttpResponse("You're voting on queetion %s." %question_id);

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



