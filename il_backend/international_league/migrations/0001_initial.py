# Generated by Django 3.2.6 on 2021-08-24 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Имя пилота', max_length=100, verbose_name='Name')),
                ('league', models.PositiveSmallIntegerField(default=None, help_text='Номер лиги, в которой выступает пилот', verbose_name='League')),
                ('image', models.ImageField(default=None, help_text='Аватарка пилота', max_length=200, upload_to='assets/images/pilots', verbose_name='Image')),
                ('is_main_pilot', models.BooleanField(default=True, help_text='Действующий или резервный пилот', verbose_name='Is main pilot')),
                ('total_score', models.SmallIntegerField(default=0, help_text='Количество очков в личном зачёте', verbose_name='Total score')),
                ('qualifying_victories_over_teammate', models.PositiveSmallIntegerField(default=0, help_text='Побед в квалификации над тиммейтом', verbose_name='Qualifying victories over teammate')),
                ('race_victories_over_teammate', models.PositiveSmallIntegerField(default=0, help_text='Побед в гонке над тиммейтом', verbose_name='Race victories over teammate')),
                ('highest_grid_position', models.PositiveSmallIntegerField(default=None, help_text='Самая высокая занятая позиция в квалификации', verbose_name='Highest grid position')),
                ('best_race_finish', models.PositiveSmallIntegerField(default=None, help_text='Самая высокая позиция занятая в гонке', verbose_name='Best race finish')),
                ('do_not_finish', models.PositiveSmallIntegerField(default=0, help_text='Количество сходов в гонках', verbose_name='Do not finish')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Название гоночной трассы', max_length=100, verbose_name='Name')),
                ('country', models.CharField(default=None, help_text='Страна, в которой проходит гонка', max_length=50, verbose_name='Country')),
                ('country_flag', models.ImageField(default=None, help_text='Флаг страны', max_length=200, upload_to='assets/images/flags', verbose_name='Country flag')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, help_text='Название команды', max_length=50, verbose_name='Name')),
                ('image', models.ImageField(default=None, help_text='Картинка команды', max_length=200, upload_to='assets/images/teams', verbose_name='Image')),
                ('total_score_league1', models.SmallIntegerField(default=0, help_text='Количество очков в кубке конструкторов лиги 1', verbose_name='Total score league 1')),
                ('total_score_league2', models.SmallIntegerField(default=0, help_text='Количество очков в кубке конструкторов лиги 1', verbose_name='Total score league 2')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_position', models.CharField(default='DNS', help_text='Позиция в гонке', max_length=20, verbose_name='Race position')),
                ('qualifying_position', models.PositiveSmallIntegerField(default=None, help_text='Позиция в квалификации', verbose_name='Qualifying position')),
                ('score', models.SmallIntegerField(default=0, help_text='Количество заработанных очков в гонке', verbose_name='Score')),
                ('penalties', models.PositiveSmallIntegerField(default=0, help_text='Штрафы полученные в гонке', verbose_name='Penalties')),
                ('best_lap', models.CharField(default='', help_text='Время лучшего круга в гонке', max_length=20, verbose_name='Best lap')),
                ('is_race_best_lap', models.BooleanField(default=False, help_text='Является ли этот результат лучшим кругом среди всех участников гонки', verbose_name='Is race best lap')),
                ('pilot', models.ForeignKey(help_text='Пилот, к которому относится данный результат', on_delete=django.db.models.deletion.CASCADE, to='international_league.pilot', verbose_name='Pilot')),
                ('race', models.ForeignKey(help_text='Трасса, к которой относится данный результат', on_delete=django.db.models.deletion.CASCADE, to='international_league.race', verbose_name='Race')),
            ],
        ),
        migrations.AddField(
            model_name='pilot',
            name='team',
            field=models.ForeignKey(blank=True, help_text='Команда в которой выступает пилот', null=True, on_delete=django.db.models.deletion.SET_NULL, to='international_league.team', verbose_name='Team'),
        ),
    ]
