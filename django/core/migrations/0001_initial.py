# Generated by Django 3.2.3 on 2021-05-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Название')),
                ('plot', models.TextField(verbose_name='Описание')),
                ('year', models.PositiveIntegerField(verbose_name='Дата')),
                ('rating', models.IntegerField(choices=[(0, 'NR - NOT Rated'), (1, 'G - General Audiences'), (2, 'PG - Parental Guidance Suggested'), (3, 'R - Restricted')], default=0, verbose_name='Рейтинг')),
                ('runtime', models.PositiveIntegerField()),
                ('website', models.URLField(blank=True)),
            ],
        ),
    ]
