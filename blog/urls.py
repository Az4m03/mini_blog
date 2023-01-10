from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('add_comments/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
]
