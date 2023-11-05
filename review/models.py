from django.db import models

# Create your models here.
class movies(models.Model):
    sno= models.AutoField(primary_key=True )
    m_name=models.CharField(max_length=30)
    release_year=models.IntegerField()
    genre=models.CharField(max_length=20,default="action")
    language=models.CharField(max_length=20,default='en')
    rating=models.IntegerField()
    portrait=models.URLField()
    landscape=models.URLField()

    def __str__(self):
        return self.m_name

# Create your models here.

class userinputs(models.Model):
    m_name= models.CharField(max_length=50)
    u_name=models.CharField(max_length=30)
    review=models.CharField(max_length=500,db_index=False)
    rating = models.IntegerField()


    def __str__(self):
        return self.u_name





