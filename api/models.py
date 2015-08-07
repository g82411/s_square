from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=128)
    session = models.CharField(max_length=35,unique=True)

class Box(models.Model):
    bid = models.AutoField(primary_key=True)
    level = models.IntegerField()
    monster = models.ForeignKey("Monster")
    owner = models.ForeignKey("User")

class Party(models.Model):
    uid = models.ForeignKey("User")
    fir = models.ForeignKey("Box",related_name="first")
    sec = models.ForeignKey("Box",related_name="second")
    thi = models.ForeignKey("Box",related_name="third")
    fou = models.ForeignKey("Box",related_name="fourth")

class UserPosition(models.Model):
    uid = models.ForeignKey("User")
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateField(auto_now=True)
    
class MonsterPosition(models.Model):
    mid = models.ForeignKey("Monster")
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateField(auto_now=True)

class Monster(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=128)
    initHP = models.IntegerField()
    initAtk = models.IntegerField()
    groHP = models.FloatField()
    groAtk = models.FloatField()

class Skill(models.Model):
    sid = models.AutoField(primary_key=True)
    target = models.CharField(max_length=40)
    function = models.TextField()


