# Generated by Django 4.0 on 2021-12-28 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeBeneficiario', models.CharField(max_length=50)),
                ('datanascBeneficiario', models.DateField(verbose_name='Bith Date')),
                ('sexoBeneficiario', models.CharField(max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
