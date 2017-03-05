# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from volley.models import Post, Team, Player
import re

class ActivitiesView(TemplateView):
    template_name = 'activities.html'

    def get_context_data(self, **kwargs):
        context = super(ActivitiesView, self).get_context_data(**kwargs)
        context['activities_active'] = True
        context['posts'] = Post.objects.all()
        return context


class RulesView(TemplateView):
    template_name = 'rules.html'

    def get_context_data(self, **kwargs):
        context = super(RulesView, self).get_context_data(**kwargs)
        context['rules_active'] = True
        return context



class RegisterView(TemplateView):
    template_name = 'register.html'
    pattern_first_name = re.compile('(\d+)\\-first_name')
    pattern_last_name = re.compile('(\d+)\\-last_name')
    pattern_class = re.compile('(\d+)\\-class')
    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        players = dict()
        email = data['email'][0]
        name = data['name'][0]
        errors = list()
        if not email or not name:
            errors.append(_(u'Pola nazwa zespołu i adres e-mail są wymagane'))

        team = Team(name=name, email=email, verified=False)
        for key in data:
            first_name = self.__search_safe(self.pattern_first_name, key)
            last_name = self.__search_safe(self.pattern_last_name, key)
            player_class = self.__search_safe(self.pattern_class, key)
            if first_name:
                if not first_name in players: players[first_name] = dict()
                players[first_name]['first_name'] = data[key][0]
            elif last_name:
                if not last_name in players: players[last_name] = dict()
                players[last_name]['last_name'] = data[key][0]
            elif player_class:
                if not player_class in players: players[player_class] = dict()
                players[player_class]['class'] = data[key][0]
        team.save()
        for p in players.values():
            if all([i in p and p[i] for i in ('first_name', 'last_name', 'class')]):
                player_obj = Player(first_name=p['first_name'], last_name=p['last_name'], school_class=p['class'], team=team)
                player_obj.save()
            else:
                errors.append(_(u'Pola imię, nazwisko i klasa są wymagane.'))
        if team.player_set.count() < 3:
            errors.append(_(u'Zespół musi mieć minimum 3 zawodników'))
        if errors:
            team.delete()
        context = self.get_context_data()
        context['post'] = True
        context['success'] = not errors
        context['errors'] = errors
        mp = [(key, players[key]) for key in players]
        context['players'] = [p[1] for p in sorted(mp)]
        context['email'] = email
        context['name'] = data['name'][0]
        return super(RegisterView, self).render_to_response(context)

    def __search_safe(self, pattern, string):
        a = pattern.search(string)
        return a.group(1) if a else None

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['post'] = False
        context['players'] = [1, 2, 3]
        context['register_active'] = True
        return context


def perform_register(request):
    if request.method == 'POST':
        print request.POST
        return HttpResponseRedirect('/thanks/')
