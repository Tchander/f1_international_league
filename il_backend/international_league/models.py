from django.db import models
from django.db.models import F, Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField('Name', max_length=50, default='', help_text='Название команды')
    url_name = models.CharField('Url name', max_length=50, default='', help_text='Адрес url', unique=True)
    image = models.ImageField('Image', upload_to='../assets/images/teams', height_field=None, width_field=None,
                              max_length=200, default=None, null=True, help_text='Картинка команды')
    total_score_league1 = models.DecimalField('Total score league 1', default=0, max_digits=5, decimal_places=1,
                                                   help_text='Количество очков в кубке конструкторов лиги 1')
    total_score_league2 = models.DecimalField('Total score league 2', default=0, max_digits=5, decimal_places=1,
                                                   help_text='Количество очков в кубке конструкторов лиги 1')


class Pilot(models.Model):
    name = models.CharField('Name', max_length=100, default='', help_text='Имя пилота')
    league = models.PositiveSmallIntegerField('League', default=2, help_text='Номер лиги, в которой выступает пилот')
    image = models.ImageField('Image', upload_to='../assets/images/pilots', height_field=None, width_field=None,
                              max_length=200, default=None, null=True, help_text='Аватарка пилота')
    is_main_pilot = models.BooleanField('Is main pilot', default=True, help_text='Действующий или резервный пилот')
    total_score = models.DecimalField('Total score', default=0, max_digits=5, decimal_places=1,
                                      help_text='Количество очков в личном зачёте')
    qualifying_victories_over_teammate = \
        models.PositiveSmallIntegerField('Qualifying victories over teammate', default=0,
                                         help_text='Побед в квалификации над тиммейтом')
    race_victories_over_teammate = models.PositiveSmallIntegerField('Race victories over teammate', default=0,
                                                                    help_text='Побед в гонке над тиммейтом')
    highest_grid_position = models.PositiveSmallIntegerField('Highest grid position', default=None, null=True,
                                                             help_text='Самая высокая занятая позиция в квалификации')
    best_race_finish = models.PositiveSmallIntegerField('Best race finish', default=None, null=True,
                                                        help_text='Самая высокая позиция занятая в гонке')
    do_not_finish = models.PositiveSmallIntegerField('Do not finish', default=0, help_text='Количество сходов в гонках')
    number_of_races_completed = models.PositiveSmallIntegerField('Number of races completed', default=0,
                                                                 help_text='Количество пройдённых гонок в сезоне')
    position_in_the_last_race = models.CharField('Position in the last race', max_length=20, default='',
                                                 help_text='Позиция в последней гонке')
    position_in_the_last_qualifying = models.CharField('Position in the last qualifying', max_length=20, default='',
                                                       help_text='Позиция в последней квалификации')
    team = models.ForeignKey(Team, verbose_name='Team', on_delete=models.SET_NULL, blank=True, null=True,
                             help_text='Команда в которой выступает пилот')


class Race(models.Model):
    name = models.CharField('Name', max_length=100, default='', help_text='Название гоночной трассы')
    country = models.CharField('Country', max_length=50, default='', help_text='Страна, в которой проходит гонка')
    country_flag = models.ImageField('Country flag', upload_to='../assets/images/flags', height_field=None,
                                     width_field=None, max_length=200, default=None, null=True, help_text='Флаг страны')
    place_in_calendar = models.PositiveSmallIntegerField('Place in calendar', default=0,
                                                         help_text='Позиция трассы в календаре')


class Result(models.Model):
    race_position = models.CharField('Race position', max_length=20, default='DNS', help_text='Позиция в гонке')
    qualifying_position = models.CharField('Qualifying position', max_length=20, default='DNQ',
                                           help_text='Позиция в квалификации')
    score = models.DecimalField('Score', default=0, max_digits=5, decimal_places=1,
                                help_text='Количество заработанных очков в гонке')
    best_lap = models.CharField('Best lap', max_length=20, default='', help_text='Время лучшего круга в гонке')
    is_race_best_lap = \
        models.BooleanField('Is race best lap', default=False,
                            help_text='Является ли этот результат лучшим кругом среди всех участников гонки')
    is_result_of_reserve_pilot = models.BooleanField('Is result of reserve pilot', default=False,
                                                     help_text='Принадлежит ли этот результат резервному пилоту')
    league = models.SmallIntegerField('League', default=1,
                                      help_text='Номер лиги к которой принадлежит данный результат')
    pilot = models.ForeignKey(Pilot, verbose_name='Pilot', on_delete=models.CASCADE,
                              help_text='Пилот, к которому относится данный результат')
    race = models.ForeignKey(Race, verbose_name='Race', on_delete=models.CASCADE,
                             help_text='Трасса, к которой относится данный результат')
    team = models.ForeignKey(Team, verbose_name='Team', on_delete=models.CASCADE,
                             help_text='Команда, к которой относится данный результат')

    def calc_score(self):
        if self.race_position == '1':
            score = 50
        elif self.race_position == '2':
            score = 40
        elif self.race_position == '3':
            score = 35
        elif self.race_position == '4':
            score = 30
        elif self.race_position == '5':
            score = 26
        elif self.race_position == '6':
            score = 22
        elif self.race_position == '7':
            score = 18
        elif self.race_position == '8':
            score = 15
        elif self.race_position == '9':
            score = 12
        elif self.race_position == '10':
            score = 10
        elif self.race_position == '11':
            score = 8
        elif self.race_position == '12':
            score = 6
        elif self.race_position == '13':
            score = 4
        elif self.race_position == '14':
            score = 2
        elif self.race_position == '15':
            score = 1
        else:
            score = 0
        if self.is_race_best_lap:
            score += 2
        return score


@receiver(pre_save, sender=Result)
def calc_pilot_score_for_race(sender, instance, *args, **kwargs):
    instance.score = instance.calc_score()


@receiver(post_save, sender=Result)
def update_pilot(sender, instance, *args, **kwargs):
    pilot = Pilot.objects.filter(id=instance.pilot.id)
    if pilot[0].league == instance.league and not instance.is_result_of_reserve_pilot and\
            pilot[0].is_main_pilot and pilot[0].team_id == instance.team_id:
        pilot.update(total_score=F("total_score") + instance.score)
        pilot.update(number_of_races_completed=F("number_of_races_completed") + 1)
        pilot.update(position_in_the_last_race=instance.race_position)
        pilot.update(position_in_the_last_qualifying=instance.qualifying_position)
        if pilot[0].league == 1:
            Team.objects.filter(id=pilot[0].team_id). \
                update(total_score_league1=F("total_score_league1") + instance.score)
        if pilot[0].league == 2:
            Team.objects.filter(id=pilot[0].team_id). \
                update(total_score_league2=F("total_score_league2") + instance.score)
        if instance.qualifying_position != 'DNQ':
            if pilot[0].highest_grid_position is None or\
                    pilot[0].highest_grid_position > int(instance.qualifying_position):
                pilot.update(highest_grid_position=int(instance.qualifying_position))
        if instance.race_position != 'DNF' and instance.race_position != 'DNS':
            if pilot[0].best_race_finish is None or pilot[0].best_race_finish > int(instance.race_position):
                pilot.update(best_race_finish=int(instance.race_position))
        if instance.race_position == 'DNF':
            pilot.update(do_not_finish=F("do_not_finish") + 1)
        teammate = Pilot.objects.filter(Q(team_id=pilot[0].team_id), Q(league=pilot[0].league), ~Q(id=pilot[0].id))
        if len(teammate) != 0:
            if pilot[0].number_of_races_completed == teammate[0].number_of_races_completed:
                if pilot[0].position_in_the_last_race != 'DNS' and teammate[0].position_in_the_last_race != 'DNS':
                    if pilot[0].position_in_the_last_race == 'DNF' and teammate[0].position_in_the_last_race != 'DNF':
                        teammate.update(race_victories_over_teammate=F("race_victories_over_teammate") + 1)
                    elif pilot[0].position_in_the_last_race != 'DNF' and teammate[0].position_in_the_last_race == 'DNF':
                        pilot.update(race_victories_over_teammate=F("race_victories_over_teammate") + 1)
                    elif pilot[0].position_in_the_last_race != 'DNF' and teammate[0].position_in_the_last_race != 'DNF':
                        if int(pilot[0].position_in_the_last_race) > int(teammate[0].position_in_the_last_race):
                            teammate.update(race_victories_over_teammate=F("race_victories_over_teammate") + 1)
                        else:
                            pilot.update(race_victories_over_teammate=F("race_victories_over_teammate") + 1)
                if pilot[0].qualifying_victories_over_teammate != 'DNQ' and\
                        teammate[0].qualifying_victories_over_teammate != 'DNQ':
                    if pilot[0].position_in_the_last_qualifying != 'DNQ':
                        if int(pilot[0].position_in_the_last_qualifying) >\
                                int(teammate[0].position_in_the_last_qualifying):
                            teammate.update(qualifying_victories_over_teammate=
                                            F("qualifying_victories_over_teammate") + 1)
                        else:
                            pilot.update(qualifying_victories_over_teammate=F("qualifying_victories_over_teammate") + 1)
    elif pilot[0].league == 2 and instance.league == 1 and instance.is_result_of_reserve_pilot:
        Team.objects.filter(id=instance.team_id).update(total_score_league1=F("total_score_league1") + instance.score)
    elif pilot[0].league == instance.league and instance.is_result_of_reserve_pilot:
        Team.objects.filter(id=instance.team_id).\
            update(total_score_league2=F("total_score_league2") + (instance.score / 2))
        pilot.update(total_score=F("total_score") + instance.score)
        pilot.update(number_of_races_completed=F("number_of_races_completed") + 1)
        pilot.update(position_in_the_last_race=instance.race_position)
        pilot.update(position_in_the_last_qualifying=instance.qualifying_position)
        if instance.race_position == 'DNF':
            pilot.update(do_not_finish=F("do_not_finish") + 1)
    elif pilot[0].league == instance.league and not instance.is_result_of_reserve_pilot and\
            pilot[0].is_main_pilot and pilot[0].team_id != instance.team_id:
        if pilot[0].league == 1:
            Team.objects.filter(id=instance.team_id). \
                update(total_score_league1=F("total_score_league1") + instance.score)
        else:
            Team.objects.filter(id=instance.team_id). \
                update(total_score_league2=F("total_score_league2") + instance.score)
        pilot.update(total_score=F("total_score") + instance.score)
        pilot.update(number_of_races_completed=F("number_of_races_completed") + 1)
        pilot.update(position_in_the_last_race=instance.race_position)
        pilot.update(position_in_the_last_qualifying=instance.qualifying_position)
    else:
        Team.objects.filter(id=instance.team_id). \
            update(total_score_league2=F("total_score_league2") + instance.score)
