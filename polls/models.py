from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.gis.db import models  #GeoDjango Model

# Create your models here.

@python_2_unicode_compatible #only if you need to support Python 2
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)		

@python_2_unicode_compatible #only if you need to support Python 2
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

# Models de Footin
# class Track(models.Model):
# 	created_date = models.DateTimefield('date created')
# 	name = models.CharField(max_length=100)

# class TrackSegment(models.Model):
# 	track = models.ForeignKey(Track, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200)

# class TrackWaypoints(models.Model):
# 	segment = models.ForeignKey(TrackSegment, on_delete=models.CASCADE)
# 	latitude = models.
# 	longitude = models.
# 	elevation = models.
# 	timestamp = models.DateTimefield('timestamp gps')
