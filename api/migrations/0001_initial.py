# Generated by Django 3.1.2 on 2020-10-06 23:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('post_type', models.BooleanField(choices=[(True, 'Boast'), (False, 'Roast')])),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
