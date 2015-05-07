from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Word(models.Model):
	word_text = models.CharField(max_length=200)
	def __str__(self):
		return self.word_text 

class Meaning(models.Model):
	meaning_text = models.CharField(max_length=1000)
	word = models.ForeignKey(Word)
	def __str__(self):
		return self.meaning_text+" -> "+self.word.word_text


class Question(models.Model):
	meaning = models.ForeignKey(Meaning)
	choice1 = models.ForeignKey(Word, related_name='question_c1')
	choice2 = models.ForeignKey(Word, related_name='question_c2')
	choice3 = models.ForeignKey(Word, related_name='question_c3')
	points = models.IntegerField(default=1)
	def __str__(self):
		return self.meaning.meaning_text+" :: "+self.choice1.word_text+" :: "+self.choice2.word_text+" :: "+self.choice3.word_text+" :: "+self.meaning.word.word_text+" = "+str(self.points)

class Student(models.Model):
	user = models.OneToOneField(User)
	points = models.IntegerField(default=0)
	questions_total = models.IntegerField(default=0)
	questions_correct = models.IntegerField(default=0)
	def __str__(self):
		return self.user.username