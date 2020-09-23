# Generated by Django 3.0.3 on 2020-09-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importDB', '0010_hrmis_v_aw_for_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_executive_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.CharField(max_length=7)),
                ('employee_name_th', models.CharField(blank=True, max_length=100, null=True)),
                ('flag_used', models.BooleanField(choices=[(True, 'ใช้'), (False, 'ไม่ใช้')], default=True)),
            ],
        ),
    ]
