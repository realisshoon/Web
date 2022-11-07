from django.contrib import admin
from django.urls import include, path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),  #서버의 루트주소/pybo/ 라는 주소에 pybo 앱 url을 연결
    path('pybo/', include('pybo.urls')),
    path('common/',include('common.urls')),
    path('',views.index,name='index'),
]
