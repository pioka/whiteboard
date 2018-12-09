# Generated by Django 2.1.3 on 2018-12-08 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20181209_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='membership',
            name='board',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='board',
            name='members',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.AddField(
            model_name='boardshare',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='board.Board'),
        ),
        migrations.AddField(
            model_name='boardshare',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='board.Board'),
        ),
    ]
