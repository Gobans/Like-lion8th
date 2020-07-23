"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #include를 통해 여러개의 urls.py 파일을 사용할 것을 명시
import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', firstapp.views.home, name='home'), #'' 내용 생략된 따옴표는 실행만 시켜도 바로 해당 function 작동 시키도록 함
    # path('first/', firstapp.views.first, name='first'),
    # path('second/', firstapp.views.second, name='second'),
    # path('third/', firstapp.views.third, name='third'),

    path('firstapp/', include('firstapp.urls')), #firstapp에 대한 요청시, firstapp.urls로 접근하여 필요 정보 획득
    path('secondapp/', include('secondapp.urls')),
]