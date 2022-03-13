from django.urls import path
from . import views

urlpatterns = [
    path(r'register/',views.RegisterView.as_view(),name='lala')
]
