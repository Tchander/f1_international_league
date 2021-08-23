from django.db import models


class Team(models.Model):
    name = models.CharField('Name', max_length=50, default=None, help_text='Название команды')
    image = models.ImageField('Image', upload_to='assets/images/teams', height_field=None,
                              width_field=None, max_length=200, default=None, help_text='Картинка команды')
    total_score_league1 = models.PositiveSmallIntegerField('Total score league 1', default=0,
                                                           help_text='Количество очков в кубке конструкторов лиги 1')
    total_score_league2 = models.PositiveSmallIntegerField('Total score league 2', default=0,
                                                           help_text='Количество очков в кубке конструкторов лиги 1')


class Pilot(models.Model):
    name = models.CharField('Name', max_length=100, default=None, help_text='Имя пилота')
    league = models.PositiveSmallIntegerField('League', default=None, help_text='Номер лиги, в которой выступает пилот')
    image = models.ImageField('Image', upload_to='assets/images/pilots', height_field=None,
                              width_field=None, max_length=200, default=None, help_text='Аватарка пилота')
    is_main_pilot = models.BooleanField('Is main pilot', default=True, help_text='Действующий или резервный пилот')
    total_score = models.PositiveSmallIntegerField('Total score', default=0,
                                                   help_text='Количество очков в личном зачёте')
    qualifying_victories_over_teammate =\
        models.PositiveSmallIntegerField('Qualifying victories over teammate', default=0,
                                         help_text='Побед в квалификации над тиммейтом')
    race_victories_over_teammate = models.PositiveSmallIntegerField('Race victories over teammate', default=0,
                                                                    help_text='Побед в гонке над тиммейтом')
    highest_grid_position = models.PositiveSmallIntegerField('Highest grid position', default=None,
                                                             help_text='Самая высокая занятая позиция в квалификации')
    best_race_finish = models.PositiveSmallIntegerField('Best race finish', default=None,
                                                        help_text='Самая высокая позиция занятая в гонке')
    do_not_finish = models.PositiveSmallIntegerField('Do not finish', default=0, help_text='Количество сходов в гонках')
    team = models.ForeignKey(Team, verbose_name='Team', on_delete=models.SET_NULL, blank=True, null=True,
                             help_text='Команда в которой выступает пилот')


class Race(models.Model):
    name = models.CharField('Name', max_length=100, default=None, help_text='Название гоночной трассы')
    country = models.CharField('Country', max_length=50, default=None, help_text='Страна, в которой проходит гонка')
    country_flag = models.ImageField('Country flag', upload_to='assets/images/flags', height_field=None,
                                     width_field=None, max_length=200, default=None, help_text='Флаг страны')


class Results(models.Model):
    race_position = models.CharField('Race position', max_length=20, default='DNS', help_text='Позиция в гонке')
    qualifying_position = models.PositiveSmallIntegerField('Qualifying position', default=None,
                                                           help_text='Позиция в квалификации')
    score = models.PositiveSmallIntegerField('Score', default=0, help_text='Количество заработанных очков в гонке')
    penalties = models.PositiveSmallIntegerField('Penalties', default=0, help_text='Штрафы полученные в гонке')
    best_lap = models.CharField('Best lap', max_length=20, default='', help_text='Время лучшего круга в гонке')
    pilot = models.ForeignKey(Pilot, verbose_name='Pilot', on_delete=models.CASCADE,
                              help_text='Пилот, к которому относится данный результат')
    race = models.ForeignKey(Race, verbose_name='Race', on_delete=models.CASCADE,
                             help_text='Трасса, к которой относится данный результат')
