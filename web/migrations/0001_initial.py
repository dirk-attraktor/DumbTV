# Generated by Django 2.0.1 on 2018-04-21 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('name', models.CharField(default='', max_length=2000)),
                ('description', models.CharField(default='', max_length=10000)),
                ('index', models.IntegerField(verbose_name=0)),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='ChannelSource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('path', models.CharField(default='', max_length=10000)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sources', to='web.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalExcludeFilter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('value', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Upcoming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('index', models.CharField(default='', max_length=20)),
                ('addon', models.CharField(default='', max_length=20)),
                ('url', models.CharField(default='', max_length=20)),
                ('title', models.CharField(default='', max_length=20)),
                ('duration', models.IntegerField(default=0)),
                ('isFolder', models.BooleanField(default=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upcoming', to='web.Channel')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
