from django.urls import path
from . import views


urlpatterns = [
    path('all', views.AuthList.as_view()),
    path('login', views.login),
    path('<pk>', views.AuthDetail.as_view()),
]
