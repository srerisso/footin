from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models  #GeoDjango Model

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

# Models de Footin
# class Track(models.Model):
# 	created_date = models.DateTimefield('date created')
# 	name = models.CharField(max_length=100)

# class TrackSegment(models.Model):
# 	track = models.ForeignKey(Track, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200)

# class TrackWaypoints(models.Model):
# 	segment = models.ForeignKey(TrackSegment, on_delete=models.CASCADE)
# 	latitude =
# 	longitude =
# 	elevation = 
# 	created = models.DateTimefield('ping gps')
