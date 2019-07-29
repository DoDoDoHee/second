from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드
    #Blog안에 있는 객체를 blogs에 담아줌
    return render(request, 'home.html', {'blogs':blogs})

    # 쿼리셋과 메소드의 정의
    # 모델.쿼리셋(objects).메소드
    # 예를 들어 blogs.all()
    # .count() .first() .last() 등등 메소드가 있음

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id번째 블로그 객체
    return render(request, 'detail.html', {'blog':blog_detail})

# 글쓰기 
def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 데이터 베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title'] # new.html에서 title 이라는 이름이 있음
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #얘를 사용하려면 timezone import해주기
    blog.save() # blog객체를 데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id)) #redirect(url) #blog.id는 정수인데 url은 문자열이므로 형변환시켜주기
    # 다 처리되고 나면 detail페이지로 가게 함
