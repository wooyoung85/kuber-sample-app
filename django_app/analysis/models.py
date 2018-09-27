from django.db import models 

class Analysis(models.Model): 
    sentence = models.CharField(max_length=200)
    polarity = models.CharField(max_length=10)

    def __str__(self): 
        return self.sentence
