# Generated by Django 3.2 on 2021-06-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choice', '0003_auto_20210530_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='event_desire',
            field=models.CharField(choices=[('cuisine', 'cuisine'), ('eventplan', 'eventplan')], default='cuisine', max_length=100),
        ),
    ]
