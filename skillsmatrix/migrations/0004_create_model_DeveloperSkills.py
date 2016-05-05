# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillsmatrix', '0003_developer_model_fix'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.CharField(max_length=30)),
                ('years_of_experience', models.IntegerField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillsmatrix.Developer')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skillsmatrix.Skill')),
            ],
        )
    ]
