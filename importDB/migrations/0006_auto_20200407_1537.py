# Generated by Django 3.0.3 on 2020-04-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importDB', '0005_prpm_r_fund_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prpm_v_grt_project_eis',
            name='camp_owner',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='prpm_v_grt_project_eis',
            name='faculty_owner',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='prpm_v_grt_project_eis',
            name='fund_type_th',
            field=models.CharField(max_length=300),
        ),
    ]
