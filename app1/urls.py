from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name = 'home'),
    path('post_twitter', views.post_twitter, name = 'post_twitter'),
    path('reply/<int:id>/', views.reply, name = 'reply'),
    path('tweet_detail/<int:id>', views.tweet_detail, name = 'tweet_detail'),
    path('process_form', views.process_form, name = 'process_form'),
]
