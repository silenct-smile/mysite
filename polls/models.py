import datetime
from django.db import models
from django.utils import timezone

"""在这个简单的投票应用中，需要创建两个模型：问题 Question 和选项 Choice。Question 模型包括问题描述和发布时间。Choice 模型有两个字段，选项描述
和当前得票数。每个选项属于一个问题。
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(self):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return  self.name

class Entry(self):
    

"""
代码非常直白。每个模型被表示为 django.db.models.Model 类的子类。每个模型有一些类变量，它们都表示模型里的一个数据库字段。
每个字段都是 Field 类的实例 - 比如，字符字段被表示为 CharField ，日期时间字段被表示为 DateTimeField 。这将告诉 Django 每个字段要处理的数据类型。
每个 Field 类实例变量的名字（例如 question_text 或 pub_date ）也是字段名，所以最好使用对机器友好的格式。你将会在 Python 代码里使用它们，而
数据库会将它们作为列名。
你可以使用可选的选项来为 Field 定义一个人类可读的名字。这个功能在很多 Django 内部组成部分中都被使用了，而且作为文档的一部分。如果某个字段没有
提供此名称，Django 将会使用对机器友好的名称，也就是变量名。在上面的例子中，我们只为 Question.pub_date 定义了对人类友好的名字。对于模型内的其它
字段，它们的机器友好名也会被作为人类友好名使用。
定义某些 Field 类实例需要参数。例如 CharField 需要一个 max_length 参数。这个参数的用处不止于用来定义数据库结构，也用于验证数据，我们稍后将会
看到这方面的内容。
Field 也能够接收多个可选参数；在上面的例子中：我们将 votes 的 default 也就是默认值，设为0。
注意在最后，我们使用 ForeignKey 定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。Django 支持所有常用的数据库关系：
多对一、多对多和一对一

通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。
迁移是 Django 对于模型定义（也就是你的数据库结构）的变化的储存形式 - 没那么玄乎，它们其实也只是一些你磁盘上的文件。如果你想的话，你可以阅读一
下你模型的迁移数据，它被储存在 polls/migrations/0001_initial.py 里。别担心，你不需要每次都阅读迁移文件，但是它们被设计成人类可读的形式，这是
为了便于你手动修改它们。
Django 有一个自动执行数据库迁移并同步管理你的数据库结构的命令 - 这个命令是 migrate，我们马上就会接触它 - 但是首先，让我们看看迁移命令会执行
哪些 SQL 语句。sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：python manage.py sqlmigrate polls 0001

请注意以下几点：

输出的内容和你使用的数据库有关，上面的输出示例使用的是 PostgreSQL。
数据库的表名是由应用名(polls)和模型名的小写形式( question 和 choice)连接而来。（如果需要，你可以自定义此行为。）
主键(IDs)会被自动创建。(当然，你也可以自定义。)
默认的，Django 会在外键字段名后追加字符串 "_id" 。（同样，这也可以自定义。）
外键关系由 FOREIGN KEY 生成。你不用关心 DEFERRABLE 部分，它只是告诉 PostgreSQL，请在事务全都执行完之后再创建外键关系。
生成的 SQL 语句是为你所用的数据库定制的，所以那些和数据库有关的字段类型，比如 auto_increment (MySQL)、 serial (PostgreSQL)和 
integer primary key autoincrement (SQLite)，Django 会帮你自动处理。那些和引号相关的事情 - 例如，是使用单引号还是双引号 - 也一样会被自动处理。
这个 sqlmigrate 命令并没有真正在你的数据库中的执行迁移 - 它只是把命令输出到屏幕上，让你看看 Django 认为需要执行哪些 SQL 语句。这在你想看看
 Django 到底准备做什么，或者当你是数据库管理员，需要写脚本来批量处理数据库时会很有用。
如果你感兴趣，你也可以试试运行 python manage.py check ;这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。
现在，再次运行 migrate 命令，在数据库里创建新定义的模型的数据表：python manage.py migrate

这个 migrate 命令选中所有还没有执行过的迁移（Django 通过在数据库中创建一个特殊的表 django_migrations 来跟踪执行过哪些迁移）并应用在数据库上 
- 也就是将你对模型的更改同步到数据库结构上。
迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据。我们会在后面的
教程中更加深入的学习这部分内容，现在，你只需要记住，改变模型需要这三步：
    编辑 models.py 文件，改变模型。
    运行 python manage.py makemigrations 为模型的改变生成迁移文件。
    运行 python manage.py migrate 来应用数据库迁移。
数据库迁移被分解成生成和应用两个命令是为了让你能够在代码控制系统上提交迁移数据并使其能在多个应用里使用；这不仅仅会让开发更加简单，也给别的开发者
和生产环境中的使用带来方便。
"""