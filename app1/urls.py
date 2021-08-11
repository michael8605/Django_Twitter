from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('', views.post_twitter, name = 'post_twitter'),
    path('reply/<int:id>/', views.reply, name = 'reply'),
    path('tweet_detail/<int:id>', views.tweet_detail, name = 'tweet_detail'),
    path('process_form', views.process_form, name = 'process_form'),
]
