from django.shortcuts import render
from .models import Tweet
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):

    def get_reply_count(tweetid):
        count = Tweet.objects.filter(parent_tweet_id=tweetid).count()
        return count

    all_tweets = Tweet.objects.all().order_by('created_at')
    for tweet in all_tweets:
        count = get_reply_count(tweet.id)
        tweet.count = count
    context = {
        'all_tweets': all_tweets,
        'count': count
    }
    return render(request, "pages/home.html", context)

def post_twitter(request):

    return render(request, "pages/post_twitter.html")

def reply(request, id):
    tweet= Tweet.objects.get(id = id)

    return render(request, "pages/reply.html", {'tweet': tweet})

def tweet_detail(request, id):
    if id is not 0:
        tweet = Tweet.objects.get(id=id)
        replies = Tweet.objects.order_by(
            '-created_at').filter(parent_tweet_id = id)
        count = Tweet.objects.filter(parent_tweet_id=id).count()

        context = {
            "tweet" : tweet,
            "replies" : replies,
            "parent_tweet_id": id,
            "count" : count
        }
        return render(request, "pages/tweet_detail.html", context)
    else:
        return render(request, "pages/tweet_detail.html", {"parent_tweet_id": None})

def process_form(request):
    if request.POST:
        file = request.FILES.get('tweet-image', None)
        name = request.POST['name']
        description = request.POST['comment']
        formtype =request.POST['formtype']
        parent_tweet_id = request.POST.get('tweetid', None)
        if description.strip() is not "":
            if file:
                with open('app1/static/userimage/' + str(file), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                imageurl = 'userimage/' + str(file)
            else:
                imageurl = None
            new_tweet = Tweet(parent_tweet_id = parent_tweet_id, name = name, text= description, image_path = imageurl)
            new_tweet.save()
        return HttpResponseRedirect(reverse('home'))