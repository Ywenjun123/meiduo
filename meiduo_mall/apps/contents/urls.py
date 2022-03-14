from django.urls import path
from . import views

urlpatterns = [
    # 首页
    path('',views.IndexView.as_view(), name='index'),
]