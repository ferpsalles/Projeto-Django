# Generated by Django 4.0 on 2021-12-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_especialidade_procedimento_medico_localatendimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='datanascBeneficiario',
            field=models.DateField(verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='datanascMedico',
            field=models.DateField(verbose_name='Birth Date'),
        ),
    ]