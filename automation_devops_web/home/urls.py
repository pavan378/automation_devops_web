from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("input",views.input,name="input"),
    path("status",views.status,name="status"),
    path("result",views.result,name="result"),
    path("logs",views.logs,name="logs"),
]
