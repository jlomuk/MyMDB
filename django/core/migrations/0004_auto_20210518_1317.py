# Generated by Django 3.2.3 on 2021-05-18 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='value',
            field=models.SmallIntegerField(choices=[(1, '👍'), (-1, '👎')], default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='voted_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'movie')},
        ),
    ]