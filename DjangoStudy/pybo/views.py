from django.shortcuts import render,HttpResponse

# Create your views here.
topics=[
{'id':1, 'title':'routing', 'body':'Routing is..'},
{'id':2, 'title':'view', 'body':'view is..'},
{'id':3, 'title':'model', 'body':'model is..'},
]

def HTMLTemplate(articleTag):
    global topics #전역변수 선언
    ol=''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f''' 
        <html>
        <body>
            <h1><a href ="/">Django</a></h1>
            <ul>
                {ol}
            </ul>
            {articleTag}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
        </html>
        '''



def index(request):
    article ='''
    <h2>Welcome</h2>
    Hello Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    global topics
    for topic in topics:
        if topic['id']==int(id):
            article=f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    article='''
        <form action="/create/"post>
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>   
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))