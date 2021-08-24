from django.db import models
from django.db.models import F
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Team(models.Model):
    name = models.CharField('Name', max_length=50, default='', help_text='Название команды')
    image = models.ImageField('Image', upload_to='assets/images/teams', height_field=None, width_field=None,
                              max_length=200, default=None, null=True, help_text='Картинка команды')
    total_score_league1 = models.SmallIntegerField('Total score league 1', default=0,
                                                   help_text='Количество очков в кубке конструкторов лиги 1')
    total_score_league2 = models.SmallIntegerField('Total score league 2', default=0,
                                                   help_text='Количество очков в кубке конструкторов лиги 1')


class Pilot(models.Model):
    name = models.CharField('Name', max_length=100, default='', help_text='Имя пилота')
    league = models.PositiveSmallIntegerField('League', default=2, help_text='Номер лиги, в которой выступает пилот')
    image = models.ImageField('Image', upload_to='assets/images/pilots', height_field=None, width_field=None,
                              max_length=200, default=None, null=True, help_text='Аватарка пилота')
    is_main_pilot = models.BooleanField('Is main pilot', default=True, help_text='Действующий или резервный пилот')
    total_score = models.SmallIntegerField('Total score', default=0, help_text='Количество очков в личном зачёте')
    qualifying_victories_over_teammate =\
        models.PositiveSmallIntegerField('Qualifying victories over teammate', default=0,
                                         help_text='Побед в квалификации над тиммейтом')
    race_victories_over_teammate = models.PositiveSmallIntegerField('Race victories over teammate', default=0,
                                                                    help_text='Побед в гонке над тиммейтом')
    highest_grid_position = models.PositiveSmallIntegerField('Highest grid position', default=None, null=True,
                                                             help_text='Самая высокая занятая позиция в квалификации')
    best_race_finish = models.PositiveSmallIntegerField('Best race finish', default=None, null=True,
                                                        help_text='Самая высокая позиция занятая в гонке')
    do_not_finish = models.PositiveSmallIntegerField('Do not finish', default=0, help_text='Количество сходов в гонках')
    team = models.ForeignKey(Team, verbose_name='Team', on_delete=models.SET_NULL, blank=True, null=True,
                             help_text='Команда в которой выступает пилот')


class Race(models.Model):
    name = models.CharField('Name', max_length=100, default='', help_text='Название гоночной трассы')
    country = models.CharField('Country', max_length=50, default='', help_text='Страна, в которой проходит гонка')
    country_flag = models.ImageField('Country flag', upload_to='assets/images/flags', height_field=None,
                                     width_field=None, max_length=200, default=None, null=True, help_text='Флаг страны')


class Result(models.Model):
    race_position = models.CharField('Race position', max_length=20, default='DNS', help_text='Позиция в гонке')
    qualifying_position = models.PositiveSmallIntegerField('Qualifying position', default=None,
                                                           help_text='Позиция в квалификации')
    score = models.SmallIntegerField('Score', default=0, help_text='Количество заработанных очков в гонке')
    penalties = models.PositiveSmallIntegerField('Penalties', default=0, help_text='Штрафы полученные в гонке')
    best_lap = models.CharField('Best lap', max_length=20, default='', help_text='Время лучшего круга в гонке')
    is_race_best_lap =\
        models.BooleanField('Is race best lap', default=False,
                            help_text='Является ли этот результат лучшим кругом среди всех участников гонки')
    pilot = models.ForeignKey(Pilot, verbose_name='Pilot', on_delete=models.CASCADE,
                              help_text='Пилот, к которому относится данный результат')
    race = models.ForeignKey(Race, verbose_name='Race', on_delete=models.CASCADE,
                             help_text='Трасса, к которой относится данный результат')

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
        return score - self.penalties


@receiver(pre_save, sender=Result)
def calc_pilot_score_for_race(sender, instance, *args, **kwargs):
    instance.score = instance.calc_score()


@receiver(post_save, sender=Result)
def update_pilot(sender, instance, *args, **kwargs):
    Pilot.objects.filter(id=instance.pilot.id).update(total_score=F("total_score")+instance.score)
