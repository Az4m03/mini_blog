from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post'),
]
