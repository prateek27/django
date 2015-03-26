from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('Enter Question Text', max_length=200)
    pub_date = models.DateTimeField()

    def get_length_of_question_text(self):
        return len(self.question_text)

    def __str__(self):
        return self.question_text[:20]

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)
    
    class Meta:
        db_table = 'choice'
        verbose_name = 'Question Choice'
        verbose_name_plural = 'Question Choicessssss'

