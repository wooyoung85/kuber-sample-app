# Create your tasks here
from __future__ import absolute_import, unicode_literals
from django_app.celery import app
from celery import task
from textblob import TextBlob


@app.task
def sentence_analysis(sentence):
    polarity = TextBlob(sentence).sentences[0].polarity
    return polarity