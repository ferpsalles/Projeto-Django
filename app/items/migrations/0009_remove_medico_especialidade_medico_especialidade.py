# Generated by Django 4.0 on 2021-12-28 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_remove_medico_especialidade_medico_especialidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='especialidade',
        ),
        migrations.AddField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.especialidade'),
            preserve_default=False,
        ),
    ]