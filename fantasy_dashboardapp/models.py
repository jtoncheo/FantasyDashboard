from django.db import models

# Create your models here.
'''This will be repurposed later to hold topic information for the website'''
class Topic(models.Model):

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''This helper method returns a string of the model'''
        return self.text 

class Entry(models.Model):
    '''Something specific about the topic.'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Returning a string representation of the model'''
        return f'{self.text[:50]}...'