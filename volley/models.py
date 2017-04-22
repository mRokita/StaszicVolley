# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tournament(models.Model):
    date = models.DateField(verbose_name=_('Data'))
    title = models.CharField(verbose_name=_('Tytuł'), max_length=128)

    class Meta:
        verbose_name = _('Turniej')
        verbose_name_plural = _('Turnieje')

    def __unicode__(self):
        return self.title


class Player(models.Model):
    SCHOOL_CHOICES = (
        ('liceum', 'Liceum'),
        ('gimnazjum', 'Gimnazjum')
    )
    first_name = models.CharField(max_length=20, verbose_name=_('Imię'))
    last_name = models.CharField(max_length=20, verbose_name=_('Nazwisko'))
    school_class = models.CharField(max_length=2, verbose_name=_('Klasa'))
    school = models.CharField(max_length=10, verbose_name=_('Szkoła'), choices=SCHOOL_CHOICES)
    team = models.ForeignKey('Team')

    class Meta:
        verbose_name = _('Zawodnik')
        verbose_name_plural = _('Zawodnicy')

    def __unicode__(self):
        return self.first_name + u' ' + self.last_name


class Team(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(verbose_name=_('E-mail'))
    verified = models.BooleanField(verbose_name=_('Zweryfikowany'))
    class Meta:
        verbose_name = _('Zespół')
        verbose_name_plural = _('Zespoły')

    def get_rank(self):
        points = 0
        for m in Match.objects.filter(team_a=self):
            points += m.score_a - m.score_b
        for m in Match.objects.filter(team_b=self):
            points += m.score_b - m.score_a
        return points

    def get_match_count(self):
        return len(Match.objects.filter(team_a=self)) + len(Match.objects.filter(team_b=self))

    def __unicode__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Team, self).__init__(*args, **kwargs)
        self.__original_verified = self.verified

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.verified != self.__original_verified and self.verified == True:
            email = EmailMessage('staszic.volley - weryfikacja zespołu', 'Twój zespół został zweryfikowany przez moderatora.\nWszystkie wiadomości dotyczące turnieju będą się pojawiały na https://volley.staszic.waw.pl\n\nPozdrawiamy,\nZespół volley.staszic', to=[self.email], from_email='volley@staszic.waw.pl')
            email.send()
        super(Team, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_verified = self.verified


class Match(models.Model):
    tournament = models.ForeignKey(verbose_name=_('Turniej'), to=Tournament)
    team_a = models.ForeignKey(verbose_name=_('Zespół A'), to=Team, related_name='team_a')
    team_b = models.ForeignKey(verbose_name=_('Zespół B'), to=Team, related_name='team_b')
    score_a = models.IntegerField(verbose_name=_('Punkty zespołu A'))
    score_b = models.IntegerField(verbose_name=_('Punkty zespołu B'))

    class Meta:
        verbose_name = _('Mecz')
        verbose_name_plural = _('Mecze')


class Post(models.Model):
    date_created = models.DateTimeField(verbose_name=_('Data utworzenia'))
    title = models.CharField(max_length = 200, verbose_name=_('Tytuł'))
    content = models.TextField(verbose_name=_('Treść'));

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posty')

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.pk == None:
            email = EmailMessage('staszic.volley - '+self.title, self.content+'\n\nPozdrawiamy,\nZespół volley.staszic', bcc=[t.email for t in Team.objects.all()], from_email='volley@staszic.waw.pl')
            email.send()
        super(Post, self).save(force_insert, force_update, *args, **kwargs)

    def __unicode__(self):
        return self.title

