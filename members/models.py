from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User
from api import settings


class Country(models.Model):
    country = models.CharField(max_length=50, unique=True)
    tel_code = models.IntegerField()

    def __str__(self):
        return self.country + '(' + str(self.tel_code) + ')'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, related_name="person", null=True, blank=True)
    photo = models.FileField(upload_to='profile/pic/%Y/%m/%d', default=None)
    firsttime = models.BooleanField(default=True)
    firstName = models.CharField('First Name', max_length=200)
    lastName = models.CharField('Last Name', max_length=200, null=True)
    nickname = models.CharField('Nick name', max_length=200)
    aim = models.CharField('Your ambition', max_length=200)
    contact = models.CharField(max_length=15, blank=True, null=True)
    country = models.ForeignKey(Country)
    resume = models.FileField(upload_to='profile/cv/%Y/%m/%d', default=None)
    ranking = models.IntegerField(blank=True, null=True, default=0)
    followers = models.ManyToManyField(User, blank=True)
    about = models.TextField()
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('ranking',)


class SkillCategory(models.Model):
    category = models.CharField('Skill Category', max_length=50, unique=True)
    ranking = models.IntegerField()

    def __str__(self):
        return str(self.category)

    class Meta:
        ordering = ('ranking',)


class Skill(models.Model):
    skill = models.CharField(max_length=50, unique=True)
    skill_category = models.ForeignKey(SkillCategory)
    profiles = models.ManyToManyField(Profile)
    ranking = models.IntegerField()

    def __str__(self):
        return str(self.skill)

    class Meta:
        ordering = ('ranking',)


class Project(models.Model):
    profile = models.ManyToManyField(Profile)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100)
    about = models.TextField()
    certificate = models.FileField(
        upload_to='profile/projects/certificates/%Y/%m/%d')

    def __str__(self):
        return str(self.title)
