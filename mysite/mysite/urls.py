from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),  #서버의 루트주소/polls/ 라는 주소에 polls 앱 url을 연결
]
