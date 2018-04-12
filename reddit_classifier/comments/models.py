from django.db import models

# Create your models here.



class Subreddit(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=256, blank=False, default='Blank subreddit title')

class Submission(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=256, blank=False, default='Blank submission title')
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)

class Sentiment(models.Model):
    name = models.CharField(max_length=128)

class Comment(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    sentiment = models.ForeignKey(Sentiment, on_delete=models.DO_NOTHING)




