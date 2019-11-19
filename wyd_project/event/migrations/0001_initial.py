# Generated by Django 2.2.6 on 2019-11-19 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Location')),
                ('rso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rso.RSO')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('rating', models.SmallIntegerField()),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='event.Event')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
