# Generated by Django 4.0.3 on 2022-04-06 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatrooms', '0002_connectedroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice1', models.IntegerField(default=0)),
                ('dice2', models.IntegerField(default=0)),
                ('dice3', models.IntegerField(default=0)),
                ('dice4', models.IntegerField(default=0)),
                ('dice5', models.IntegerField(default=0)),
                ('palifico', models.BooleanField(default=False)),
                ('ready', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatrooms.chatroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbdice', models.IntegerField(default=0)),
                ('valuedice', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]