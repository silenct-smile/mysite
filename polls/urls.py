from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
# ex: /polls/5/
    path('<int:question_id>/detail',views.detail,name='detail'),
# ex: /polls/5/results/
    path('<int:question_id>/results/',views.results,name='results'),
# ex: /polls/5/vote/
    path('<int:question_id>/votes',views.vote,name='vote'),
]

"""
path() route
    route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找
    到匹配的项。这些准则不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 https://www.example.com/myapp/ 时，它会尝试匹配 myapp/ 。
    处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。
path() 参数： view
    当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式
    传入。稍后，我们会给出一个例子。
path() 参数： kwargs
    任意个关键字参数可以作为一个字典传递给目标视图函数。本教程中不会使用这一特性。
path() 参数： name
    为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。
"""