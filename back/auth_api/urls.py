from django.urls import path
from . import views


urlpatterns = [
    # path('all', views.AuthList.as_view()),
    path('all', views.auth_list),
    path('create_auth', views.create_auth),
    path('<pk>', views.auth_detail),
    path('login', views.login),
    # path('<pk>', views.AuthDetail.as_view()),
]
