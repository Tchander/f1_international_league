from django.db import models


class Team(models.Model):
    name = models.CharField('Name', max_length=50, default=None)
    image = models.ImageField('Image', upload_to='static/images/teams',
                              height_field=None, width_field=None, max_length=200, default=None)
    total_score_league1 = models.PositiveSmallIntegerField('Total score league 1', default=0)
    total_score_league2 = models.PositiveSmallIntegerField('Total score league 2', default=0)


class Pilot(models.Model):
    name = models.CharField('Name', max_length=100, default=None)
    league = models.PositiveSmallIntegerField('League', default=None)
    image = models.ImageField('Image', upload_to='static/images/pilots',
                              height_field=None, width_field=None, max_length=200, default=None)
    is_main_pilot = models.BooleanField('Is main pilot', default=True)
    total_score = models.PositiveSmallIntegerField('Total score', default=0)
    qualifying_victories_over_teammate = \
        models.PositiveSmallIntegerField('Qualifying victories over teammate', default=0)
    race_victories_over_teammate = models.PositiveSmallIntegerField('Race victories over teammate', default=0)
    highest_grid_position = models.PositiveSmallIntegerField('Highest grid position', default=None)
    best_race_finish = models.PositiveSmallIntegerField('Best race finish', default=None)
    dnf = models.PositiveSmallIntegerField('DNF', default=0)
    team = models.ForeignKey(Team, verbose_name='Team', on_delete=models.SET_NULL, blank=True, null=True)


class Race(models.Model):
    name = models.CharField('Name', max_length=100, default=None)
    country = models.CharField('Country', max_length=50, default=None)
    country_flag = models.ImageField('Country flag', upload_to='static/images/flags',
                                     height_field=None, width_field=None, max_length=200, default=None)


class Results(models.Model):
    race_position = models.CharField('Race position', max_length=20, default='DNS')
    qualifying_position = models.PositiveSmallIntegerField('Qualifying position', default=None)
    score = models.PositiveSmallIntegerField('Score', default=0)
    penalties = models.PositiveSmallIntegerField('Penalties', default=0)
    best_lap = models.CharField('Best lap', max_length=20, default='')
    pilot = models.ForeignKey(Pilot, verbose_name='Pilot', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, verbose_name='Race', on_delete=models.CASCADE)
