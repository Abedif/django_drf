# Generated by Django 5.0.4 on 2024-05-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_skills_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='team',
            name='instagram',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='team',
            name='linkdin',
            field=models.CharField(default='#', max_length=220),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter',
            field=models.CharField(default='#', max_length=220),
        ),
    ]