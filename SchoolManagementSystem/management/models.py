from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class FacultyOtherInfo(models.Model):
    f_id = models.CharField(max_length=10)
    contact = models.CharField(max_length=12) 
    subject = models.CharField(max_length=30)
    userid = models.CharField(max_length=50,blank=True)
    cid = models.CharField(max_length=100,blank=True)
    
    def __unicode__(self):
        return self.contact

class MainUserOtherInfo(models.Model):    
    f_id = models.CharField(max_length=10)
    userid = models.CharField(max_length=50)
    cid = models.CharField(max_length=100)
    
class Subjects(models.Model):
    sub_id = models.CharField(max_length=10)
    subject = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.sub_id
    
class Timeing(models.Model):
    sub_id = models.CharField(max_length=10)
    p_start_time = models.DateTimeField()
    p_end_time = models.DateTimeField()     


class FacultyAlocations(models.Model):
    f_id = models.CharField(max_length=10)#f_id --faculty id
    sub_id = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    timing = models.DateTimeField()